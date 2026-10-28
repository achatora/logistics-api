from decimal import Decimal

import pytest

from app.common.address import Address
from app.shipment.item import Item
from app.shipment.recipient import Recipient
from app.shipment.shipment import Shipment
from app.shipment.shipment_status import ShipmentStatus


@pytest.fixture
def valid_shipment_data():
    address = Address(
        street_address="10 Main Street",
        city="Warsaw",
        postal_code="00-001",
        country="Poland",
    )

    recipient = Recipient(
        name="John Doe",
        phone_number="123456789",
        address=address,
    )

    return {
        "sender_name": "Jane Doe",
        "sender_phone_number": "987654321",
        "sender_address": address,
        "recipient": recipient,
        "items": [
            Item(name="Box", weight=Decimal(5), quantity=2),
            Item(name="Laptop", weight=Decimal(3), quantity=1),
        ],
    }


def test_shipment_can_be_created(valid_shipment_data):
    shipment = Shipment(**valid_shipment_data)

    assert shipment.sender_name == "Jane Doe"
    assert shipment.status == ShipmentStatus.PENDING


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("sender_name", ""),
        ("sender_name", "   "),
        ("sender_phone_number", ""),
        ("sender_phone_number", "   "),
        ("sender_address", None),
        ("recipient", None),
        ("items", None),
        ("items", []),
    ],
)
def test_shipment_rejects_invalid_data(valid_shipment_data, field, value):
    valid_shipment_data[field] = value

    with pytest.raises(ValueError):
        Shipment(**valid_shipment_data)


def test_shipment_calculates_total_weight(valid_shipment_data):
    shipment = Shipment(**valid_shipment_data)

    assert shipment.total_weight == Decimal(13)
