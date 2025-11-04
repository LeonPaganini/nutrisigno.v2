"""
Repository layer for sessions.

Stubbed functions for creating and retrieving authentication sessions.
Actual implementations should interact with your chosen database or
token store.
"""

from typing import Optional

from ..schemas.session import SessionRead


def create_session(db_session, user_id: str) -> SessionRead:
    """Create a new session for a user.

    Parameters
    ----------
    db_session
        Database session or connection.
    user_id : str
        ID of the user.

    Returns
    -------
    SessionRead
        Newly created session.  Stubbed with static values.
    """
    return SessionRead(session_id="session-id", user_id=user_id)


def get_session(db_session, session_id: str) -> Optional[SessionRead]:
    """Retrieve a session by its ID.

    Parameters
    ----------
    db_session
        Database session or connection.
    session_id : str
        Identifier of the session.

    Returns
    -------
    Optional[SessionRead]
        Session if found, otherwise ``None``.  Stub always returns a
        placeholder session.
    """
    return SessionRead(session_id=session_id, user_id="user-id")