from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from config.dependencies import get_db, get_current_user, oauth2_scheme
from config import security
from config.settings import settings
from config.redis_client import redis_client
from auth import schemas, services
from users.models import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
):
    user = services.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        subject=user.email, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
def logout(
    current_user: Annotated[User, Depends(get_current_user)],
    token: str = Depends(oauth2_scheme)
):
    # Blacklist the token in Redis
    # Calculate time to live (TTL) based on token expiration, or just set a standard TTL
    redis_client.setex(f"blacklist:{token}", settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60, "true")
    return {"message": "Successfully logged out"}
