"""
Response submission routes.

Clients post answers to the questionnaire to the ``/responses`` endpoint.
This skeleton stores the answers in memory and returns a calculated
calorie target, inferred sign and element.  In a production system
these values would be derived from the answers and persisted to
PostgreSQL.
"""

import uuid
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field


class ResponseCreate(BaseModel):
    """Model for creating a new response.

    For simplicity the answers are represented as an arbitrary JSON
    object.  Clients should supply at least the required fields
    (weight, height, water intake, Bristol scale, urine color, etc.),
    but this skeleton does not enforce any schema.
    """

    answers: dict = Field(default_factory=dict)
    calorie_target: int | None = None


router = APIRouter()


@router.post("/")
async def create_response(response: ResponseCreate) -> dict:
    """Accept questionnaire responses and compute basics.

    Parameters
    ----------
    response : ResponseCreate
        Answers submitted by the client.

    Returns
    -------
    dict
        A summary containing a placeholder response ID and derived
        nutritional parameters.
    """
    # Generate a placeholder response ID
    resp_id = str(uuid.uuid4())
    # Stub calculation of calorie target and sign/element.  These
    # values would normally come from the logic in the service layer.
    calorie_target = response.calorie_target or 1500
    sign = "aries"
    element = "fogo"
    return {
        "resp_id": resp_id,
        "calorie_target": calorie_target,
        "sign": sign,
        "element": element,
    }