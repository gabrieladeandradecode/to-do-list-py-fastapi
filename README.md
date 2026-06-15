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

1) Set up the environment:
python -m venv venv

2) Install dependencies:
pip install -r requirements.txt

3) For this app, it's necessary to donwload PostgreSQL:
Donwload PostgreSQL here --> https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
After donwloading, add in your system's PATH environment the path to the PostgreSQL bin folder.
Note: Save your login credentials (user and password) for later.
Remember not to use specials characters as #, $, @.. use only letters and numbers.

To ensure it's working, run this in the VS Code terminal: 
psql --version

4) Create a .env file and add your login credentials in the following format:
DATABASE_URL = postgresql://postgres:password@localhost/tasks
Ensure to alter the part "password" to your login credential.

5) To connect to the database, run this in the VS Code terminal: 
psql -U postgres
It will ask for your password and the input might be invisible for you, but that's normal. After typing, press Enter.
If it shows:
postgres=#
It worked.

6) Create the database "tasks" and remember to use the ; because is a SQL command:
CREATE DATABASE tasks;
Result : CREATE DATABASE

Note: if you want to change your login credentials, here's the command:
ALTER USER postgres WITH PASSWORD 'password';

Now to close the postgres terminal, run:
\q

8) To run the API, do: 
uvicorn main:app --reload

It will show an URL. Click on it.

