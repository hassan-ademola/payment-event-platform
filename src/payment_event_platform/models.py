from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field, field_validator


class EventType(StrEnum):
    CREATED = "payment.created"
    AUTHORISED = "payment.authorised"
    CAPTURED = "payment.captured"
    FAILED = "payment.failed"
    REFUNDED = "payment.refunded"


class PaymentEvent(BaseModel):
    event_id: str
    payment_id: str
    merchant_id: str
    customer_id: str

    event_type: EventType

    amount_minor: int = Field(ge=0, strict=True)
    currency: str = Field(pattern=r"^[A-Z]{3}$")

    event_time: datetime
    received_time: datetime

    @field_validator(
        "event_id",
        "payment_id",
        "merchant_id",
        "customer_id",
    )
    @classmethod
    def validate_id(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("ID must not be empty")

        return value