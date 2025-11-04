"""
Pydantic models for user-related data.

These models are used both for validation of incoming request bodies
and for type hints in the service and repository layers.
"""

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    dob: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    user_id: str

    class Config:
        orm_mode = True