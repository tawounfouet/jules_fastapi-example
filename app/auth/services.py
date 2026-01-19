from sqlalchemy.orm import Session
from app.users import services as user_services
from app.core import security

def authenticate_user(db: Session, email: str, password: str):
    user = user_services.get_user_by_email(db, email)
    if not user:
        return False
    if not security.verify_password(password, user.hashed_password):
        return False
    return user
