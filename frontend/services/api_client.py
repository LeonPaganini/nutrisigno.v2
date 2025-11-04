"""
Stubbed API client for the Streamlit frontend.

In a real implementation these functions would make HTTP requests to
the FastAPI backend.  Here they return static data to illustrate
integration points.
"""

import uuid


def login(email: str, dob: str) -> dict:
    """Authenticate the user and return a session token."""
    return {"session": str(uuid.uuid4())}


def submit_answers(answers: dict) -> dict:
    """Submit questionnaire answers and compute basic parameters."""
    resp_id = str(uuid.uuid4())
    calorie_target = answers.get("calorie_target", 1500)
    return {
        "resp_id": resp_id,
        "calorie_target": calorie_target,
        "sign": "aries",
        "element": "fogo",
    }


def request_report(resp_id: str) -> dict:
    """Request report generation and return its ID."""
    return {"report_id": str(uuid.uuid4()), "status": "queued"}


def get_report(report_id: str) -> dict:
    """Retrieve a report by its ID."""
    return {
        "report_id": report_id,
        "status": "ready",
        "metrics": {
            "imc": 22.5,
            "agua_recomendada_l": 2.5,
            "macro_balance": {"p": 30, "c": 45, "g": 25},
        },
        "blocks": [
            {"type": "heading", "text": "Resumo"},
            {"type": "paragraph", "text": "Este é um relatório de exemplo."},
        ],
    }


def generate_image(report_id: str) -> dict:
    """Trigger image generation and return the asset info."""
    return {"asset_id": str(uuid.uuid4()), "url": "/assets/images/placeholder.png"}


def generate_pdf(report_id: str) -> dict:
    """Trigger PDF generation and return the asset info."""
    return {"asset_id": str(uuid.uuid4()), "url": "/assets/pdfs/placeholder.pdf"}