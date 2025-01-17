from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    password: str

class UserOut(BaseModel):
    name: str
    email: str
    added_on: datetime  # This is expected to always be a datetime object
    updated_on: Optional[datetime]  # Make updated_on optional

    class Config:
        orm_mode = True

class Login(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserUpdate(BaseModel):
    name: Optional[str] = None  # Use Optional to indicate that the field can be None
    email: Optional[str] = None  # Same for email
