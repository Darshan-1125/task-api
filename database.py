import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, Field, create_engine

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://taskuser:taskpassword@localhost:5432/tasksdb"
)

engine = create_engine(
    DATABASE_URL,
    echo=True
)


class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    done: bool = False


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)