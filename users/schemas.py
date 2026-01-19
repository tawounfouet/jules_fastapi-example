from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool
    avatar_url: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
