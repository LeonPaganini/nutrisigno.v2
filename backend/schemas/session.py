"""
Pydantic models for authentication sessions.
"""

from pydantic import BaseModel


class SessionRead(BaseModel):
    session_id: str
    user_id: str
    issued_at: str | None = None
    expires_at: str | None = None

    class Config:
        orm_mode = True