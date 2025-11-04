"""
Asset model.

Represents a generated asset (image or PDF) associated with a report.
Assets store metadata about the file and its linkage back to the
report.  The path field should point to a location on disk or in
object storage where the file resides.
"""

from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from .base import Base


class Asset(Base):
    __tablename__ = "assets"

    asset_id = Column(String, primary_key=True, index=True)
    report_id = Column(String, ForeignKey("reports.report_id"), nullable=False, index=True)
    kind = Column(String, nullable=False)  # 'image' or 'pdf'
    path = Column(String, nullable=False)
    sha256 = Column(String, nullable=True)
    size_bytes = Column(Integer, nullable=True)
    mime = Column(String, nullable=True)
    width = Column(Integer, nullable=True)
    height = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=True)