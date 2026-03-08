from fastapi import Depends, HTTPException
from app.utils.roles import UserRole
from app.core.security import get_current_user


def require_admin(user=Depends(get_current_user)):

    if user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Admin access required")

    return user