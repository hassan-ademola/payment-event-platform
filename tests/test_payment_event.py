import pytest
from pydantic import ValidationError

from payment_event_platform.models import PaymentEvent


def test_valid_payment_event() -> None:
    event = PaymentEvent(
        event_id="evt_001",
        payment_id="pay_001",
        merchant_id="merchant_001",
        customer_id="customer_001",
        event_type="payment.created",
        amount_minor=5000,
        currency="GBP",
        event_time="2026-10-12T10:00:00Z",
        received_time="2026-10-12T10:00:01Z",
    )

    assert event.amount_minor == 5000

    print(event.model_dump_json())


def test_negative_amount_is_rejected() -> None:
    with pytest.raises(ValidationError):
        PaymentEvent(
            event_id="evt_002",
            payment_id="pay_002",
            merchant_id="merchant_001",
            customer_id="customer_001",
            event_type="payment.created",
            amount_minor=-5000,
            currency="GBP",
            event_time="2026-10-12T10:00:00Z",
            received_time="2026-10-12T10:00:01Z",
        )