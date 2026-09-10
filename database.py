from sqlmodel import SQLModel, Field, create_engine, Session, select

DATABASE_URL = "sqlite:///tasks.db"

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

    with Session(engine) as session:
        existing_tasks = session.exec(select(Task)).all()

        if len(existing_tasks) == 0:
            example_tasks = [
                Task(
                    title="Learn FastAPI",
                    done=False
                ),
                Task(
                    title="Buy milk",
                    done=True
                ),
                Task(
                    title="Finish assignment",
                    done=False
                )
            ]

            session.add_all(example_tasks)
            session.commit()