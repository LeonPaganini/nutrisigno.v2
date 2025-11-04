"""
Payment model.

Tracks payments made through external providers such as Mercado Pago.
This skeleton stores only minimal metadata; for a real implementation
you should include fields for currency, refund status, and more.
"""

from sqlalchemy import Column, String, DateTime, Integer, JSON, ForeignKey
from .base import Base


class Payment(Base):
    __tablename__ = "payments"

    pay_id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.user_id"), nullable=True, index=True)
    report_id = Column(String, ForeignKey("reports.report_id"), nullable=True, index=True)
    provider_id = Column(String, nullable=False)  # e.g. Mercado Pago payment ID
    status = Column(String, nullable=False)
    amount_cents = Column(Integer, nullable=False)
    received_at = Column(DateTime, nullable=True)
    raw = Column(JSON, nullable=True)