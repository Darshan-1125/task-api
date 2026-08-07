# Task API

A simple CRUD (Create, Read, Update, Delete) API built using **FastAPI**. This project manages a to-do list using an **in-memory list** (no database). It was developed as part of an internship assignment to learn REST APIs, HTTP methods, validation, and Swagger UI.

---

## Features

- Create a new task
- View all tasks
- View a task by ID
- Update a task
- Delete a task
- Input validation
- Proper HTTP status codes
- Interactive Swagger UI documentation

---

## Technologies Used

- Python 3
- FastAPI
- Uvicorn
- Pydantic

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Darshan-1125/task-api.git
```

### 2. Go to the project folder

```bash
cd task-api
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
uvicorn main:app --reload
```

The API will start on:

```
http://localhost:8000
```

---

## Swagger Documentation

Interactive API documentation is available at:

```
http://localhost:8000/docs
```

You can test all endpoints directly using the **Try it out** button.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Get API information |
| GET | `/health` | Check server health |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update an existing task |
| DELETE | `/tasks/{task_id}` | Delete a task |

---

## Example Request

### Create a Task

**Request**

```http
POST /tasks
```

```json
{
    "title": "Learn FastAPI"
}
```

**Response**

```json
{
    "id": 4,
    "title": "Learn FastAPI",
    "done": false
}
```

Status Code:

```
201 Created
```

---

## Example curl Command

```bash
curl -i -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Learn FastAPI"}'
```

Example Response:

```text
HTTP/1.1 201 Created
content-type: application/json

{
  "id": 4,
  "title": "Learn FastAPI",
  "done": false
}
```

---

## Project Structure

```
task-api/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
    └── swagger-ui.png
```

---

## HTTP Status Codes Used

| Status Code | Meaning |
|-------------|---------|
| 200 | Success |
| 201 | Resource Created |
| 204 | Resource Deleted Successfully |
| 400 | Invalid Request |
| 404 | Task Not Found |

---

## Testing

The API was tested using:

- Swagger UI (`/docs`)
- Browser
- curl

The complete CRUD cycle (Create, Read, Update, Delete) works successfully.

---

## Note

This project stores data in an **in-memory list**. Since no database is used, all tasks are lost whenever the server is restarted. This behavior is intentional for this assignment.

---

## Author

**Darshan S**

GitHub: https://github.com/Darshan-1125