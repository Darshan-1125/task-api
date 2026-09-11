# Task API — SQLite Database

A simple CRUD Task API built using Python, FastAPI, Uvicorn, and SQLite.

This project is an extension of the previous in-memory Task API. The task data is now stored permanently in a SQLite database.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLModel
- SQLite
- Swagger UI
- Git & GitHub

## Features

- Create tasks
- Read all tasks
- Read a task by ID
- Update tasks
- Delete tasks
- SQLite persistent storage
- Automatic database creation
- Automatic table creation
- Three example tasks are inserted when the database is empty
- Swagger UI for API testing

## Why SQLite?

SQLite was chosen because it is lightweight and easy to use for a small backend project.

It does not require a separate database server. The entire database is stored in a single file called `tasks.db`.

This makes SQLite useful for learning database concepts and building small applications.

## Database Location

The SQLite database is stored as:

https://github.com/Darshan-1125/task-api
tasks.db

