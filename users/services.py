from sqlalchemy.orm import Session
from sqlalchemy import select
from users.models import User
from users.schemas import UserCreate
from config.security import get_password_hash
from config.storage import s3_client, create_bucket_if_not_exists
from config.settings import settings
from fastapi import UploadFile
import uuid

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

def update_user_avatar(db: Session, user_id: int, file: UploadFile):
    user = db.scalar(select(User).where(User.id == user_id))
    if not user:
        return None

    bucket_name = settings.MINIO_BUCKET
    create_bucket_if_not_exists(bucket_name)

    file_extension = file.filename.split(".")[-1]
    file_name = f"avatars/{user_id}_{uuid.uuid4()}.{file_extension}"

    try:
        s3_client.upload_fileobj(
            file.file,
            bucket_name,
            file_name,
            ExtraArgs={"ContentType": file.content_type}
        )

        # Construct URL
        # For local minio, it's usually http://localhost:9000/bucket/key
        # For real S3, it's different.
        protocol = "https" if settings.MINIO_SECURE else "http"
        url = f"{protocol}://{settings.MINIO_ENDPOINT}/{bucket_name}/{file_name}"

        user.avatar_url = url
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None
