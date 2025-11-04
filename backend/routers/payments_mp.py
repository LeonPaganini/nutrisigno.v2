"""
Mercado Pago webhook integration.

This route accepts POST requests from the Mercado Pago webhook.  It
logs the request payload and returns a simple acknowledgement.  In a
complete implementation it would update payment status in the
database, associate payments with reports, and handle idempotency.
"""

from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/")
async def mercado_pago_webhook(request: Request) -> dict:
    """Handle Mercado Pago webhook events.

    Parameters
    ----------
    request : Request
        Incoming request containing the webhook payload.

    Returns
    -------
    dict
        An acknowledgement message.
    """
    payload = await request.json()
    # In a real implementation you would verify the signature, update
    # payment status, and persist the payload for audit.
    # This skeleton simply echoes the payload size.
    return {
        "status": "received",
        "received_bytes": len(str(payload).encode("utf-8")),
    }