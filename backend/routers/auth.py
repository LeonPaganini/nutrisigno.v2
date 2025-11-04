"""
Authentication routes for the NutriSigno API.

The authentication layer for this skeleton is intentionally simple: it
accepts an email address and date of birth and returns a stubbed
response.  In a real implementation you would verify that the user
exists (or create them on the fly), generate a secure session token,
and set an HTTP-only cookie on the response.
"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    """Request model for user login."""

    email: EmailStr
    dob: str  # date of birth in YYYY-MM-DD format


router = APIRouter()


@router.post("/login")
async def login(req: LoginRequest) -> dict:
    """Authenticate a user.

    This stubbed endpoint always returns success.  In a complete
    implementation this function would verify the provided email and
    date of birth against a data store, issue a session token, and
    attach it as an HTTP-only cookie.

    Parameters
    ----------
    req : LoginRequest
        User credentials submitted from the client.

    Returns
    -------
    dict
        A placeholder response indicating success.
    """
    # In a real implementation you would perform lookup and token
    # creation here.  We always succeed for the skeleton.
    return {"message": "Logged in (stub)", "session": "session-token"}