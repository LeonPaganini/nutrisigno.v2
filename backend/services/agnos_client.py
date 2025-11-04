"""
Stub client for interacting with the Agnos AI service.

This skeleton does not include any network calls.  The real client
would send a JSON payload to the Agnos API, handle retries and
timeouts, and return the parsed response.
"""

from typing import Any


class AgnosClient:
    """A stubbed client for the Agnos AI API."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def generate_report(self, payload: dict) -> dict:
        """Generate a report using the AI service.

        Parameters
        ----------
        payload : dict
            Input data required by the AI model.

        Returns
        -------
        dict
            A placeholder response mimicking the expected structure.
        """
        # In a real implementation you would make an HTTP request here.
        return {
            "model_version": "agnos_nutrisigno_v1",
            "summary": "Relatório gerado pelo stub.",
            "metrics": {
                "imc": 22.5,
                "agua_recomendada_l": 2.5,
                "macro_balance": {"p": 30, "c": 45, "g": 25},
            },
            "behavior_modifiers": [],
            "general_insights": [],
            "nutrition_insights": [],
            "risk_notes": [],
            "recommended_calorie_target": 1500,
            "substitution_strategy": {"rule": "macro_dominante+calorias", "tolerance_pct": 2.0},
            "blocks": [
                {"type": "heading", "text": "Resumo"},
                {"type": "paragraph", "text": "Este é um relatório gerado pelo cliente stub."},
            ],
        }