from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Task API",
    description="A simple CRUD API built using FastAPI.",
    version="1.0"
)

# In-memory database (temporary storage)
tasks = [
    {
        "id":1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id":2,
        "title": "Buy milk",
        "done": True
    },
    {
        "id":3,
        "title": "Finish assignment",
        "done": False
    }
]

class TaskCreate(BaseModel):
    title: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

# Endpoints
@app.get("/",summary="Get API information")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health",summary="Check server health")
def health():
    return {
        "status": "ok"
    }

@app.get("/tasks",summary="Get all tasks")
def task():
    return tasks

@app.get("/tasks/{task_id}",summary="Get a task by ID")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(
    status_code=404,
    detail=f"Task {task_id} not found"
    )

@app.post("/tasks", status_code=201,summary="Create a new task")
def create_task(task: TaskCreate):
    if task.title is None or task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )
    new_id = tasks[-1]["id"] + 1
    new_task = {
        "id": new_id,
        "title": task.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

@app.put("/tasks/{task_id}",summary="Update a task")
def update_task(task_id: int, updated_task: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if updated_task.title.strip() == "":
                raise HTTPException(
                    status_code=400,
                    detail="Title cannot be empty"
                )
            if updated_task.title is None or updated_task.title.strip() == "":
                raise HTTPException(
                status_code=400,
                detail="Title is required"
                )
            if updated_task.done is None:
                raise HTTPException(
                status_code=400,
                detail="Done field is required"
                )
            task["title"] = updated_task.title
            task["done"] = updated_task.done
            return task
    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )

@app.delete("/tasks/{task_id}", status_code=204,summary="Delete a task")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )