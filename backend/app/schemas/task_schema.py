from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str
    status: str = "todo"


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None