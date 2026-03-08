from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.task import Task
from app.core.security import get_db, get_current_user

router = APIRouter(prefix="/dashboard")


@router.get("/stats")
def stats(db: Session = Depends(get_db),
          user=Depends(get_current_user)):

    result = (
        db.query(Task.status, func.count(Task.id))
        .filter(Task.owner_id == user.id)
        .group_by(Task.status)
        .all()
    )

    return dict(result)