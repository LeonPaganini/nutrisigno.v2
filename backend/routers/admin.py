"""
Admin routes for NutriSigno.

Provides aggregate metrics useful for internal dashboards such as
number of reports generated, number of paid reports, and revenue.
Stubbed values are returned for illustration purposes.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/metrics")
async def metrics() -> dict:
    """Return aggregated metrics for admin dashboards.

    Returns
    -------
    dict
        Aggregated counts and revenue.  All values are stubbed.
    """
    return {
        "totals": {
            "reports": 0,
            "paid": 0,
            "upsell": 0,
        },
        "by_day": [],
        "revenue": [],
    }