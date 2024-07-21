from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

class GridItem(BaseModel):
    id: int
    name: str
    age: int
    country: str

grid_data = [
    {"id": 1, "name": "John Doe", "age": 30, "country": "USA"},
    {"id": 2, "name": "Jane Smith", "age": 25, "country": "Canada"},
]

@app.get('/api/grid-data/', response_model=list[GridItem]) # this is saying the api is going to return a list of GridItem's (pydantic model) 
async def get_grid_data():
    return grid_data

@app.get('/')
async def read_index():
    return FileResponse('static/index.html')




