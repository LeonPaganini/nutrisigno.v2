"""
SQLAlchemy base class for all models.

All ORM models in the backend should inherit from ``Base`` to ensure
they are properly registered with SQLAlchemy's metadata and to allow
Alembic to detect schema changes.
"""

from sqlalchemy.orm import declarative_base

# Create a single declarative base for all models
Base = declarative_base()