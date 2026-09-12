from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from contextlib import asynccontextmanager

from database import create_db_and_tables
from service import TaskService


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    title="Task API",
    description="A simple CRUD API built using FastAPI.",
    version="1.0",
    lifespan=lifespan
)


class TaskCreate(BaseModel):
    title: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


task_service = TaskService()


# Endpoints

@app.get("/", summary="Get API information")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health", summary="Check server health")
def health():
    return {
        "status": "ok"
    }


@app.get("/tasks", summary="Get all tasks")
def get_tasks():
    return task_service.get_all_tasks()


@app.get("/tasks/{task_id}", summary="Get a task by ID")
def get_task(task_id: int):
    return task_service.get_task(task_id)


@app.post("/tasks", status_code=201, summary="Create a new task")
def create_task(task: TaskCreate):
    return task_service.create_task(task.title)


@app.put("/tasks/{task_id}", summary="Update a task")
def update_task(task_id: int, updated_task: TaskUpdate):
    return task_service.update_task(
        task_id,
        updated_task.title,
        updated_task.done
    )


@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):
    task_service.delete_task(task_id)
    return