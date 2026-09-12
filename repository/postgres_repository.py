from sqlmodel import Session, select

from database import engine, Task


class PostgresRepository:

    def get_all(self):
        with Session(engine) as session:
            return session.exec(select(Task)).all()

    def get_by_id(self, task_id: int):
        with Session(engine) as session:
            return session.get(Task, task_id)

    def create(self, title: str):
        new_task = Task(
            title=title,
            done=False
        )

        with Session(engine) as session:
            session.add(new_task)
            session.commit()
            session.refresh(new_task)

            return new_task

    def update(self, task_id: int, title: str, done: bool):
        with Session(engine) as session:
            task = session.get(Task, task_id)

            if task is None:
                return None

            task.title = title
            task.done = done

            session.add(task)
            session.commit()
            session.refresh(task)

            return task

    def delete(self, task_id: int):
        with Session(engine) as session:
            task = session.get(Task, task_id)

            if task is None:
                return False

            session.delete(task)
            session.commit()

            return True