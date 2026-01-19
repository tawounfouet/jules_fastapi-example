from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.dependencies import get_db, get_current_user
from blog import schemas, services
from users.models import User

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=schemas.PostRead)
def create_post(
    post: schemas.PostCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    return services.create_post(db=db, post=post, user_id=current_user.id)

@router.get("/", response_model=list[schemas.PostRead])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = services.get_posts(db, skip=skip, limit=limit)
    return posts
