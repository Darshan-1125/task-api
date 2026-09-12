from fastapi import HTTPException

from repository.postgres_repository import PostgresRepository


class TaskService:

    def __init__(self):
        self.repository = PostgresRepository()

    def get_all_tasks(self):
        return self.repository.get_all()

    def get_task(self, task_id: int):
        task = self.repository.get_by_id(task_id)

        if task is None:
            raise HTTPException(
                status_code=404,
                detail=f"Task {task_id} not found"
            )

        return task

    def create_task(self, title: str):
        if title is None or title.strip() == "":
            raise HTTPException(
                status_code=400,
                detail="Title cannot be empty"
            )

        return self.repository.create(title)

    def update_task(self, task_id: int, title: str, done: bool):
        if title is None:
            raise HTTPException(
                status_code=400,
                detail="Title is required"
            )

        if title.strip() == "":
            raise HTTPException(
                status_code=400,
                detail="Title cannot be empty"
            )

        if done is None:
            raise HTTPException(
                status_code=400,
                detail="Done field is required"
            )

        task = self.repository.update(
            task_id,
            title,
            done
        )

        if task is None:
            raise HTTPException(
                status_code=404,
                detail=f"Task {task_id} not found"
            )

        return task

    def delete_task(self, task_id: int):
        deleted = self.repository.delete(task_id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail=f"Task {task_id} not found"
            )
