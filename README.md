# 🎛️ Master Data Source Manager

## 🖼️ Project Screenshot
[Insert your project screenshot here]

## 🚀 Project Overview

In many companies, business users need to edit data at the data warehouse level. This project demonstrates one approach to enable this, using master data source system precedence as an example. 

The application allows business users to decide which source systems should be used to pull data for columns that have data from multiple source systems. This is crucial for maintaining data quality and consistency across the organization.

## ✨ Features

- 🌐 Interactive web interface for viewing and editing column precedence data
- ⚡ Real-time updates using AG Grid
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
5. 📈 The updated data is then reflected in downstream data processes, ensuring that data is pulled from the correct source systems according to the latest precedence rules.

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

The application is designed to be deployed on Azure App Service, allowing for easy scaling and management. Deployment instructions are included in the project documentation.

## 🔮 Future Enhancements

- 👤 Implement user authentication and role-based access control
- 📝 Add audit logging for all changes
- 🖥️ Develop a more comprehensive UI for managing other aspects of master data
- 🔍 Integrate with data quality monitoring tools

## 💡 Why This Matters

Effective master data management is crucial for businesses to maintain data consistency and accuracy across various systems. By providing a user-friendly interface for managing data source precedence, this tool empowers business users to directly influence data quality without needing technical intervention for every change. This can lead to more agile data management practices and improved overall data reliability in the organization.

## 🏁 Getting Started

(Include instructions for setting up the project locally, including any necessary environment variables, dependencies, and how to run the application)

## 🤝 Contributing

This is a portfolio project, but suggestions and feedback are welcome. Please open an issue or submit a pull request if you have ideas for improvements.

## 📄 License

[Include your chosen license here]
