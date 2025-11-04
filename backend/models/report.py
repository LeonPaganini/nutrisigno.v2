"""
Report model.

Represents a generated report.  Contains references to the user and
response records and holds the status of the report as well as
structured output such as metrics and content blocks.  For brevity
all JSON fields are typed as generic JSON.
"""

from sqlalchemy import Column, String, DateTime, ForeignKey, JSON
from .base import Base


class Report(Base):
    __tablename__ = "reports"

    report_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=False, index=True)
    resp_id = Column(String, ForeignKey("responses.resp_id"), nullable=False, index=True)
    status = Column(String, nullable=False)
    model_version = Column(String, nullable=True)
    cache_hit = Column(String, nullable=True)
    calorie_target = Column(String, nullable=True)
    signo = Column(String, nullable=True)
    elemento = Column(String, nullable=True)
    metrics = Column(JSON, nullable=True)
    blocks = Column(JSON, nullable=True)
    created_at = Column(DateTime, nullable=True)