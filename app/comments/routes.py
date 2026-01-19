from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.comments import schemas, services
from app.users.models import User
from app.blog import services as blog_services

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/", response_model=schemas.CommentRead)
def create_comment(
    comment: schemas.CommentCreate,
    current_user: Annotated[User, Depends(get_current_user)],
    db: Session = Depends(get_db)
):
    # Verify post exists
    post = blog_services.get_post(db, post_id=comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    return services.create_comment(db=db, comment=comment, user_id=current_user.id)

@router.get("/", response_model=list[schemas.CommentRead])
def read_comments(post_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = services.get_comments_by_post(db, post_id=post_id, skip=skip, limit=limit)
    return comments
