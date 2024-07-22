from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, constr, field_validator
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
from cachetools import TTLCache
from datetime import timedelta
from dotenv import load_dotenv
import os
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


load_dotenv()


limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


app.mount('/static', StaticFiles(directory='static'), name="static")

# Set up BigQuery client
creds_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
credentials = service_account.Credentials.from_service_account_file(creds_path)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# Define your dataset and table
dataset_id = 'datamart'
table_id = 'column_precedence'

cache = TTLCache(maxsize=1, ttl=timedelta(minutes=15).total_seconds())

class ColumnPrecedence(BaseModel):
    column: str
    first_source: str
    second_source: str
    third_source: str

    @field_validator('first_source','second_source','third_source')
    def validate_source(cls, v, field): 
        valid_sources = {'CRM','ERP','Marketing'}
        if v not in valid_sources: 
            raise ValueError(f'{field.name} must be one of {valid_sources}')
        return v

@app.get('/')
async def display_index():
    return FileResponse('static/index.html')


@app.get("/api/column-precedence/")
@limiter.limit("5/minute")
async def read_column_precedence(request: Request):
    if 'column_precedence' not in cache:
        query = f"""
        SELECT column, first_source, second_source, third_source
        FROM `{dataset_id}.{table_id}`
        """
        df = client.query(query).to_dataframe()
        cache['column_precedence'] = df.to_dict('records')

    return cache['column_precedence']

@app.put("/api/column-precedence/batch")
@limiter.limit("2/minute")
async def update_column_precedence_batch(request: Request, items: list[ColumnPrecedence]):
    try:
        # Prepare the data for BigQuery
        rows_to_update = [item.model_dump() for item in items]
        
        # Create a temporary table for the updates
        temp_table_id = f"{dataset_id}.temp_updates"
        job_config = bigquery.LoadJobConfig(
            schema=[
                bigquery.SchemaField("column", "STRING"),
                bigquery.SchemaField("first_source", "STRING"),
                bigquery.SchemaField("second_source", "STRING"),
                bigquery.SchemaField("third_source", "STRING"),
            ],
            write_disposition="WRITE_TRUNCATE",
        )
        
        job = client.load_table_from_json(rows_to_update, temp_table_id, job_config=job_config)
        job.result()  # Wait for the job to complete
        
        # Perform the update
        update_query = """
        UPDATE `{}.{}` main
        SET 
            first_source = updates.first_source,
            second_source = updates.second_source,
            third_source = updates.third_source
        FROM `{}` updates
        WHERE main.column = updates.column
        """.format(dataset_id, table_id, temp_table_id)
        
        query_job = client.query(update_query)
        query_job.result()  # Wait for the job to complete
        
        # Clean up the temporary table
        client.delete_table(temp_table_id)
        
        # Clear the cache
        cache.clear()
        
        return {"message": f"Successfully updated {len(items)} rows"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
