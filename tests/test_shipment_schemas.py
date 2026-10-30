import pytest
from pydantic import ValidationError

from app.api.schemas.shipment import CreateShipmentRequest


@pytest.fixture
def valid_shipment_request():
    return {
        "sender_name": "Alfred",
        "sender_phone_number": "123456789",
        "sender_address": {
            "street_address": "Main Street 1",
            "city": "Warsaw",
            "postal_code": "00-001",
            "country": "Poland",
        },
        "recipient": {
            "name": "John",
            "phone_number": "987654321",
            "address": {
                "street_address": "Second Street 2",
                "city": "Krakow",
                "postal_code": "30-001",
                "country": "Poland",
            },
        },
        "items": [
            {
                "name": "Laptop",
                "weight": "2.5",
                "quantity": 1,
            }
        ],
    }


def test_accepts_valid_shipment_request(valid_shipment_request):
    request = CreateShipmentRequest(**valid_shipment_request)

    assert request.sender_name == "Alfred"


@pytest.mark.parametrize("field", ["sender_name", "sender_phone_number"])
def test_rejects_blank_sender_fields(valid_shipment_request, field):
    valid_shipment_request[field] = "   "

    with pytest.raises(ValidationError):
        CreateShipmentRequest(**valid_shipment_request)


@pytest.mark.parametrize(
    "field",
    ["street_address", "city", "postal_code", "country"],
)
def test_rejects_blank_sender_address_fields(valid_shipment_request, field):
    valid_shipment_request["sender_address"][field] = "   "

    with pytest.raises(ValidationError):
        CreateShipmentRequest(**valid_shipment_request)


@pytest.mark.parametrize("field", ["name", "phone_number"])
def test_rejects_blank_recipient_fields(valid_shipment_request, field):
    valid_shipment_request["recipient"][field] = "   "

    with pytest.raises(ValidationError):
        CreateShipmentRequest(**valid_shipment_request)


@pytest.mark.parametrize(
    "field",
    ["street_address", "city", "postal_code", "country"],
)
def test_rejects_blank_recipient_address_fields(valid_shipment_request, field):
    valid_shipment_request["recipient"]["address"][field] = "   "

    with pytest.raises(ValidationError):
        CreateShipmentRequest(**valid_shipment_request)


def test_rejects_blank_item_name(valid_shipment_request):
    valid_shipment_request["items"][0]["name"] = "   "

    with pytest.raises(ValidationError):
        CreateShipmentRequest(**valid_shipment_request)


@pytest.mark.parametrize("weight", ["0", "-1", "-2.5"])
def test_rejects_non_positive_item_weight(valid_shipment_request, weight):
    valid_shipment_request["items"][0]["weight"] = weight

    with pytest.raises(ValidationError):
        CreateShipmentRequest(**valid_shipment_request)


@pytest.mark.parametrize("quantity", [0, -1, -5])
def test_rejects_non_positive_item_quantity(valid_shipment_request, quantity):
    valid_shipment_request["items"][0]["quantity"] = quantity

    with pytest.raises(ValidationError):
        CreateShipmentRequest(**valid_shipment_request)


def test_converts_request_to_domain_shipment(valid_shipment_request):
    request = CreateShipmentRequest(**valid_shipment_request)

    shipment = request.convert_to_domain()

    assert shipment.sender_name == "Alfred"
    assert shipment.sender_address.city == "Warsaw"
    assert shipment.recipient.name == "John"
    assert len(shipment.items) == 1
    assert shipment.items[0].name == "Laptop"
