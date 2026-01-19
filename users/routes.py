from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from config.dependencies import get_db, get_current_user
from users import schemas, services
from users.models import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return services.create_user(db=db, user=user)

@router.get("/", response_model=list[schemas.UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = services.get_users(db, skip=skip, limit=limit)
    return users

@router.post("/me/avatar", response_model=schemas.UserRead)
def upload_avatar(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    updated_user = services.update_user_avatar(db, current_user.id, file)
    if not updated_user:
        raise HTTPException(status_code=500, detail="Failed to upload avatar")
    return updated_user
