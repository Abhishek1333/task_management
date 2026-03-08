from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from app.schemas.task_schema import TaskCreate, TaskUpdate
from app.models.task import Task
from app.core.security import get_db, get_current_user

router = APIRouter(prefix="/tasks")


@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):

    if not task.title or not task.description:
        raise HTTPException(status_code=400, detail="Title and description required")

    new_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        owner_id=user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("/")
def list_tasks(
    page: int = 1,
    limit: int = 10,
    status: str | None = Query(None),
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):

    query = db.query(Task).filter(Task.owner_id == user.id)

    if status:
        query = query.filter(Task.status == status)

    tasks = query\
        .offset((page - 1) * limit)\
        .limit(limit)\
        .all()

    return tasks


@router.put("/{task_id}")
def update_task(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
    ):

    task = db.query(Task).get(task_id)

    for key, value in data.dict(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()

    return task


@router.delete("/{task_id}")
def delete_task(
    task_id: int,            
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
    ):

    task = db.query(Task).get(task_id)

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}