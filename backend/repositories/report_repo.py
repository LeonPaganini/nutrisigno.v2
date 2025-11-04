"""
Repository layer for reports.

Contains stubbed methods for creating, retrieving, and updating
reports.  Real implementations should use SQLAlchemy session
operations.
"""

from typing import Optional

from ..schemas.report import ReportRead


def create_report(db_session, user_id: str, resp_id: str) -> ReportRead:
    """Create a new report record.

    Parameters
    ----------
    db_session
        Database session or connection.
    user_id : str
        ID of the user.
    resp_id : str
        ID of the response on which the report will be based.

    Returns
    -------
    ReportRead
        Newly created report.  Stubbed with static values.
    """
    return ReportRead(
        report_id="report-id",
        user_id=user_id,
        status="queued",
        model_version=None,
        cache_hit=None,
        calorie_target=None,
        signo=None,
        elemento=None,
        metrics=None,
        blocks=None,
        created_at=None,
    )


def get_report(db_session, report_id: str) -> Optional[ReportRead]:
    """Retrieve a report by its ID.

    Parameters
    ----------
    db_session
        Database session or connection.
    report_id : str
        Unique identifier of the report.

    Returns
    -------
    Optional[ReportRead]
        Report if found, otherwise ``None``.  Always returns a
        placeholder report in this skeleton.
    """
    return ReportRead(
        report_id=report_id,
        user_id="user-id",
        status="ready",
        model_version="agnos_nutrisigno_v1",
        cache_hit="false",
        calorie_target="1500",
        signo="aries",
        elemento="fogo",
        metrics={},
        blocks=[],
        created_at=None,
    )