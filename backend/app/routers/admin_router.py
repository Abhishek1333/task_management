from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.core.security import get_db
from app.core.dependencies import require_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users")
def get_all_users(
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    users = db.query(User).all()

    return users