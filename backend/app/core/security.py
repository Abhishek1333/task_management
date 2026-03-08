from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.config import JWT_SECRET, ALGORITHM

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)


def create_token(data: dict):

    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=2)

    return jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)


def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)):

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
    except:
        raise HTTPException(401, "Invalid token")

    user = db.query(User).get(user_id)

    if not user:
        raise HTTPException(401, "User not found")

    return user