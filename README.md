# 🎛️ Master Data Manager

## 🖼️ Project Screenshot
![image](images/project-screenshot.png)


## 🚀 Project Overview

In many companies, business users need to edit data at the data warehouse level. This project demonstrates one approach to enable this, using master data source system precedence as an example. 

The application allows business users to decide which source systems should be used to pull data for columns that have data from multiple source systems. This is crucial for maintaining data quality and consistency across the organization.

## ✨ Features

- 🌐 Interactive web interface for viewing and editing column precedence data
- ⚡ Data viewing and editing with AG Grid
- 🔙 Backend API built with FastAPI
- 💾 Data storage and retrieval using Google BigQuery
- ☁️ Deployment-ready for Azure App Service

## 🛠️ Tech Stack

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/120px-HTML5_logo_and_wordmark.svg.png" alt="HTML5" width="50"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/120px-JavaScript-logo.png" alt="JavaScript" width="50"/>
  <img src="https://www.ag-grid.com/images/ag-grid-logo.png" alt="AG Grid" height="50"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/121px-Python-logo-notext.svg.png" alt="Python" width="50"/>
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="100"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Google-BigQuery-Logo.svg/120px-Google-BigQuery-Logo.svg.png" alt="BigQuery" width="70"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Microsoft_Azure.svg/150px-Microsoft_Azure.svg.png" alt="Azure" width="50"/>
</p>

- Frontend: HTML, JavaScript, AG Grid
- Backend: Python, FastAPI
- Database: Google BigQuery
- Deployment: Azure App Service

## 🔧 How It Works

1. 📊 The application displays a grid showing columns and their current source system precedence (first, second, and third choices).
2. ✏️ Business users can edit the precedence directly in the grid.
3. 💾 Changes are collected and can be saved in bulk.
4. 🔄 The backend processes these changes and updates the BigQuery table.
5. 📈 The updated data is then reflected in downstream data processes (in theory, not actually), ensuring that data is pulled from the correct source systems according to the latest precedence rules.

## 🧩 Key Components

- `main.py`: FastAPI application handling API requests and BigQuery interactions
- `index.html`: Frontend interface using AG Grid for data display and editing
- BigQuery table: Stores the column precedence data

## 🔒 Security Considerations

- 🚦 Rate limiting to prevent API abuse
- ✅ Input validation to ensure data integrity
- 🛡️ Prepared statements for BigQuery interactions to prevent SQL injection
- 🔐 Authentication and authorization (to be implemented for production use)

## 🚀 Deployment

The application is designed to be deployed on Azure App Service, allowing for easy scaling and management.

## 🔮 Future Enhancements

- 👤 Implement user authentication and role-based access control
- 📝 Add audit logging for all changes
- 🖥️ Develop a more comprehensive UI for managing other aspects of master data

## 💡 Why This Matters

A perennial problem I've found working for tons of clients is the need for business users to write data at the data warehouse level (such as defining precedence order of source systems). I've created solutions to this using Streamlit, Excel, Django, Sharepoint, and PowerApps. I wanted to test out FastAPI + AgGrid as another option. I quite like this solutions simplicity (relative to something like Django) but total control over the front end (compared to something like Streamlit). 

