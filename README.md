# To-Do List API (FastAPI)

Project A3 for University - API with Python using FastAPI and PostgreSQL.

Tests:
Postman
Swagger UI(/docs)

Tech Stack:
Python
FastAPI
PostgreSQL

Installation steps:

1) For this app, it's necessary to donwload PostgreSQL:
Donwload PostgreSQL here --> https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
After donwloading, add in your system's PATH environment the path to the PostgreSQL bin folder.
Note: Save your login credentials (user and password) for later.

To ensure it's working, run this in the VS Code terminal: 
psql --version

3) Set up the environment:
python -m venv venv

4) Install dependencies:
pip install -r requirements.txt

5) Create an file .env and pass the login and password in the following format:
postgresql://user:password


To connect the database

To run the API, do: 
uvicorn main:app --reload
