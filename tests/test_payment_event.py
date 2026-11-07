import json

import pytest
from pydantic import ValidationError

from payment_event_platform.models import PaymentEvent


@pytest.fixture
def valid_event_data() -> dict[str, object]:
    return {
        "event_id": "evt_001",
        "payment_id": "pay_001",
        "merchant_id": "merchant_001",
        "customer_id": "customer_001",
        "event_type": "payment.created",
        "amount_minor": 5000,
        "currency": "GBP",
        "event_time": "2026-10-12T10:00:00Z",
        "received_time": "2026-10-12T10:00:01Z",
    }


def test_valid_payment_event(valid_event_data : dict[str,object]) -> None:
    event = PaymentEvent(
        **valid_event_data,
    )
    json_data = json.loads(event.model_dump_json())

    assert json_data["currency"] == "GBP"
    assert json_data["event_type"] == "payment.created"
    assert json_data["amount_minor"] == 5000

@pytest.mark.parametrize(
    "amount_minor",
    [-1, -5000, 1.5, "5000"]
)
def test_negative_amount_is_rejected(valid_event_data : dict[str,object],
                                     amount_minor: object) -> None:
    with pytest.raises(ValidationError):
        invalid_event_data = {**valid_event_data,"amount_minor":amount_minor}
        PaymentEvent(
            **invalid_event_data
        )

@pytest.mark.parametrize(
    "currency",
    ["gbp", "GB", "POUNDS", "123"]
)
def test_invalid_currency_is_rejected(valid_event_data : dict[str,object], 
                                      currency: str) -> None:
    with pytest.raises(ValidationError):
        invalid_event_data = {**valid_event_data,"currency":currency}
        PaymentEvent(
            **invalid_event_data
        )

@pytest.mark.parametrize(
    "event_type",
    [
        "payment.unknown",
        "authorised",
        "",
        "payment.AUTHORISED",
    ],
)
def test_invalid_event_type_is_rejected(valid_event_data : dict[str,object],
                                        event_type: str) -> None:
    with pytest.raises(ValidationError):
        invalid_event_data = {**valid_event_data,"event_type":event_type}
        PaymentEvent(
            **invalid_event_data
        )

@pytest.mark.parametrize(
    "field_name",
    ["event_id", "payment_id", "merchant_id", "customer_id"],
)
@pytest.mark.parametrize(
    "invalid_id",
    ["", "   "],
)
def test_invalid_id_is_rejected(
    valid_event_data: dict[str, object],
    field_name: str,
    invalid_id: str,
) -> None:
    invalid_data = {
        **valid_event_data,
        field_name: invalid_id,
    }

    with pytest.raises(ValidationError):
        PaymentEvent(**invalid_data)