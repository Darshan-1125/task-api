# Task API — FastAPI + PostgreSQL + Docker

A simple CRUD Task API built using **FastAPI**, **SQLModel**, **PostgreSQL**, and **Docker Compose**.

This project started as a basic FastAPI CRUD API and was progressively upgraded to use a real PostgreSQL database running inside Docker.

---

## Technologies

- Python 3.13
- FastAPI
- Pydantic
- SQLModel
- PostgreSQL 17
- psycopg2
- Docker
- Docker Compose
- Uvicorn
- Git & GitHub
- Swagger UI

---

## Architecture

The application follows a layered architecture:

https://github.com/Darshan-1125/task-api
Client / Swagger UI
        |
        v
   FastAPI Routes
      main.py
        |
        v
    TaskService
     service.py
        |
        v
 PostgresRepository
repository/postgres_repository.py
        |
        v
    PostgreSQL
        |
        v
 Docker Persistent Volume