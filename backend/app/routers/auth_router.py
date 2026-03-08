from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user_schema import UserCreate, UserLogin
from app.models.user import User
from app.core.security import hash_password, verify_password, create_token, get_db, get_current_user

router = APIRouter()


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return {"message": "Email already exists"}

    db_user = User(
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()

    return {"message": "User created"}
    

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(400, "Invalid credentials")

    if not verify_password(user.password, db_user.password):
        raise HTTPException(400, "Invalid credentials")

    token = create_token({"user_id": db_user.id})

    return {"access_token": token}

@router.get("/info")
def user_info(user: User = Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
        "role": user.role
    }