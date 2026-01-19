from sqlalchemy.orm import Session
from sqlalchemy import select
from app.comments.models import Comment
from app.comments.schemas import CommentCreate

def create_comment(db: Session, comment: CommentCreate, user_id: int):
    db_comment = Comment(**comment.model_dump(), owner_id=user_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments_by_post(db: Session, post_id: int, skip: int = 0, limit: int = 100):
    return db.scalars(select(Comment).where(Comment.post_id == post_id).offset(skip).limit(limit)).all()
