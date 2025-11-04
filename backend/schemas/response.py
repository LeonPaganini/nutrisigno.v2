"""
Pydantic models for questionnaire responses.
"""

from pydantic import BaseModel, Field


class ResponseCreate(BaseModel):
    answers: dict = Field(default_factory=dict)
    calorie_target: int | None = None


class ResponseRead(BaseModel):
    resp_id: str
    user_id: str | None = None
    payload: dict

    class Config:
        orm_mode = True