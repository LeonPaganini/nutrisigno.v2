"""
Response model.

Stores a user's questionnaire answers as a JSON object along with
metadata such as creation time.  Responses are linked to users and
serve as the input for report generation.
"""

from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from .base import Base


class Response(Base):
    __tablename__ = "responses"

    resp_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False, index=True)
    payload = Column(JSON, nullable=False)
    created_at = Column(DateTime, nullable=True)