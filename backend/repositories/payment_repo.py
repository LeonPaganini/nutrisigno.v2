"""
Repository layer for payments.

Handles creation and retrieval of payment records.  For this skeleton
the functions simply return placeholder data.  Real implementations
should persist payments in the database and handle reconciliation.
"""

from typing import Optional

from ..schemas.payment import PaymentRead


def create_payment(db_session, provider_id: str, status: str, amount_cents: int) -> PaymentRead:
    """Create a new payment record.

    Parameters
    ----------
    db_session
        Database session or connection.
    provider_id : str
        Payment ID from the provider (e.g. Mercado Pago).
    status : str
        Payment status.
    amount_cents : int
        Amount in cents.

    Returns
    -------
    PaymentRead
        Newly created payment.  Stubbed with static values.
    """
    return PaymentRead(
        pay_id="payment-id",
        user_id=None,
        report_id=None,
        provider_id=provider_id,
        status=status,
        amount_cents=amount_cents,
        received_at=None,
        raw={},
    )


def get_payment(db_session, pay_id: str) -> Optional[PaymentRead]:
    """Retrieve a payment by its ID.

    Parameters
    ----------
    db_session
        Database session or connection.
    pay_id : str
        Identifier of the payment.

    Returns
    -------
    Optional[PaymentRead]
        Payment if found, otherwise ``None``.  Always returns
        placeholder values in this skeleton.
    """
    return PaymentRead(
        pay_id=pay_id,
        user_id=None,
        report_id=None,
        provider_id="provider-id",
        status="pending",
        amount_cents=0,
        received_at=None,
        raw={},
    )