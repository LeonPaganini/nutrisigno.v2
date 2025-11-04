"""
Session model.

Represents an authentication session issued after a successful login.
Sessions are tied to a user and expire after a fixed duration.
"""

from sqlalchemy import Column, String, DateTime, ForeignKey
from .base import Base


class Session(Base):
    __tablename__ = "sessions"

    session_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False, index=True)
    issued_at = Column(DateTime, nullable=True)
    expires_at = Column(DateTime, nullable=True)