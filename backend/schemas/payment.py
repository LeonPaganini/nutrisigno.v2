"""
Pydantic models for payments.
"""

from pydantic import BaseModel


class PaymentRead(BaseModel):
    pay_id: str
    user_id: str | None = None
    report_id: str | None = None
    provider_id: str
    status: str
    amount_cents: int
    received_at: str | None = None
    raw: dict | None = None

    class Config:
        orm_mode = True