from sqlalchemy.orm import Session
from sqlalchemy import select
from app.users.models import User
from app.users.schemas import UserCreate
from app.core.security import get_password_hash

def get_user_by_email(db: Session, email: str):
    return db.scalar(select(User).where(User.email == email))

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.scalars(select(User).offset(skip).limit(limit)).all()
