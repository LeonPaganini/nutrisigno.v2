"""
User model.

Represents a registered user in the system.  In this skeleton,
authentication is simplified and this model is minimal.  Real
implementations would include hashed passwords, timestamps, and other
attributes required by the application's authentication strategy.
"""

from sqlalchemy import Column, String, Date, DateTime
from .base import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    dob = Column(Date, nullable=False)
    created_at = Column(DateTime, nullable=True)