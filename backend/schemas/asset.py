"""
Pydantic models for generated assets.
"""

from pydantic import BaseModel


class AssetRead(BaseModel):
    asset_id: str
    report_id: str
    kind: str
    path: str
    sha256: str | None = None
    size_bytes: int | None = None
    mime: str | None = None
    width: int | None = None
    height: int | None = None
    created_at: str | None = None

    class Config:
        orm_mode = True