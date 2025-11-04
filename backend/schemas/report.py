"""
Pydantic models for reports.
"""

from pydantic import BaseModel, Field


class ReportRequest(BaseModel):
    resp_id: str


class ReportRead(BaseModel):
    report_id: str
    user_id: str | None = None
    status: str
    model_version: str | None = None
    cache_hit: str | None = None
    calorie_target: str | None = None
    signo: str | None = None
    elemento: str | None = None
    metrics: dict | None = None
    blocks: list[dict] | None = None
    created_at: str | None = None

    class Config:
        orm_mode = True