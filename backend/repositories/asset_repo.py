"""
Repository layer for assets.

Stub functions for creating and retrieving assets.  Assets include
images and PDFs generated from reports.
"""

from typing import Optional

from ..schemas.asset import AssetRead


def create_asset(db_session, report_id: str, kind: str, path: str) -> AssetRead:
    """Create a new asset record.

    Parameters
    ----------
    db_session
        Database session or connection.
    report_id : str
        ID of the report the asset belongs to.
    kind : str
        Asset type, either ``image`` or ``pdf``.
    path : str
        Location of the file.

    Returns
    -------
    AssetRead
        Newly created asset.  Stubbed with static values.
    """
    return AssetRead(
        asset_id="asset-id",
        report_id=report_id,
        kind=kind,
        path=path,
        sha256=None,
        size_bytes=None,
        mime=None,
        width=None,
        height=None,
        created_at=None,
    )


def get_asset(db_session, asset_id: str) -> Optional[AssetRead]:
    """Retrieve an asset by its ID.

    Parameters
    ----------
    db_session
        Database session or connection.
    asset_id : str
        Unique identifier of the asset.

    Returns
    -------
    Optional[AssetRead]
        Asset if found, otherwise ``None``.  Always returns a
        placeholder asset in this skeleton.
    """
    return AssetRead(
        asset_id=asset_id,
        report_id="report-id",
        kind="image",
        path=f"/assets/images/{asset_id}.png",
        sha256=None,
        size_bytes=None,
        mime="image/png",
        width=None,
        height=None,
        created_at=None,
    )