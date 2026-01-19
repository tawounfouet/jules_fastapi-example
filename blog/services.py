from sqlalchemy.orm import Session
from sqlalchemy import select
from blog.models import Post
from blog.schemas import PostCreate

def create_post(db: Session, post: PostCreate, user_id: int):
    db_post = Post(**post.model_dump(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.scalars(select(Post).offset(skip).limit(limit)).all()

def get_post(db: Session, post_id: int):
    return db.scalar(select(Post).where(Post.id == post_id))
