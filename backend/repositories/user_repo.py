"""
Repository layer for users.

This module provides functions for creating and retrieving users from
the database.  In this skeleton we do not implement any actual
persistence; instead, stub functions illustrate the intended API.
"""

from typing import Optional

from ..schemas.user import UserCreate, UserRead


def create_user(db_session, user: UserCreate) -> UserRead:
    """Create a new user.

    Parameters
    ----------
    db_session
        Database session or connection.
    user : UserCreate
        Pydantic model containing user fields.

    Returns
    -------
    UserRead
        Newly created user.  Stubbed with static values.
    """
    # NOTE: Replace with actual database insertion logic
    return UserRead(user_id="user-id", email=user.email, dob=user.dob)


def get_user_by_email(db_session, email: str) -> Optional[UserRead]:
    """Retrieve a user by email.

    Parameters
    ----------
    db_session
        Database session or connection.
    email : str
        Email address of the user.

    Returns
    -------
    Optional[UserRead]
        User if found, otherwise ``None``.  Stub always returns a
        placeholder user.
    """
    # NOTE: Replace with actual query logic
    return UserRead(user_id="user-id", email=email, dob="1970-01-01")