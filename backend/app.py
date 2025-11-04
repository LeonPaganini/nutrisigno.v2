"""
Main FastAPI application for the NutriSigno backend.

This module creates and configures a FastAPI application.  It imports
the various routers defined in the ``backend.routers`` package and
registers them with appropriate URL prefixes and tag names.  The
resulting app is exposed as a module-level ``app`` for use with
ASGI servers such as ``uvicorn``.

This file is intentionally light on implementation logic to serve as
an entry point for the skeleton application.  Real business logic
should live in the routers, services, and repository layers.
"""

from fastapi import FastAPI

from .routers import (
    auth,
    responses,
    reports,
    assets,
    payments_mp,
    admin,
)


def create_app() -> FastAPI:
    """Create and configure the FastAPI app.

    Returns
    -------
    FastAPI
        Configured FastAPI application ready to run.
    """
    app = FastAPI(title="NutriSigno API", version="0.1.0")
    app.include_router(auth.router, prefix="/auth", tags=["auth"])
    app.include_router(responses.router, prefix="/responses", tags=["responses"])
    app.include_router(reports.router, prefix="/reports", tags=["reports"])
    app.include_router(assets.router, prefix="/assets", tags=["assets"])
    app.include_router(payments_mp.router, prefix="/payments/mp", tags=["payments"])
    app.include_router(admin.router, prefix="/admin", tags=["admin"])
    return app


# Create a global ASGI application instance
app = create_app()