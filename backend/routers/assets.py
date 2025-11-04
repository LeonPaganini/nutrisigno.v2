"""
Asset generation routes.

Endpoints here allow clients to trigger the generation of images and
PDFs from a ready report.  The skeleton returns placeholder asset
identifiers and URLs.  Actual rendering logic should live in the
``backend.services`` package.
"""

import uuid
from fastapi import APIRouter

router = APIRouter()


@router.post("/{report_id}/image")
async def generate_image(report_id: str) -> dict:
    """Generate a shareable image for the report.

    Returns
    -------
    dict
        A placeholder asset ID and URL where the image could be
        downloaded.
    """
    asset_id = str(uuid.uuid4())
    url = f"/assets/images/{asset_id}.png"
    return {"asset_id": asset_id, "url": url}


@router.post("/{report_id}/pdf")
async def generate_pdf(report_id: str) -> dict:
    """Generate a PDF version of the report.

    Returns
    -------
    dict
        A placeholder asset ID and URL where the PDF could be
        downloaded.
    """
    asset_id = str(uuid.uuid4())
    url = f"/assets/pdfs/{asset_id}.pdf"
    return {"asset_id": asset_id, "url": url}