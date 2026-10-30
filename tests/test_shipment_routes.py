from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_shipment():
    response = client.post(
        "/shipments",
        json={
            "sender_name": "Alfred",
            "sender_phone_number": "+48123456789",
            "sender_address": {
                "street_address": "Main Street 10",
                "city": "Warsaw",
                "postal_code": "00-001",
                "country": "Poland",
            },
            "recipient": {
                "name": "John",
                "phone_number": "+48987654321",
                "address": {
                    "street_address": "Second Street 5",
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
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["sender_name"] == "Alfred"
    assert data["recipient"]["name"] == "John"
    assert data["status"] == "pending"
    assert data["total_weight"] == "2.5"
    assert "shipment_id" in data
    assert "created_at" in data

    # check if API only exposes the
    # fields we explicitly allow
    assert set(data.keys()) == {
        "shipment_id",
        "sender_name",
        "sender_phone_number",
        "sender_address",
        "recipient",
        "items",
        "status",
        "created_at",
        "total_weight",
    }


def test_create_shipment_rejects_invalid_request():
    response = client.post(
        "/shipments",
        json={
            "sender_name": "",  # empty sender_name
            "sender_phone_number": "+48123456789",
            "sender_address": {
                "street_address": "Main Street 10",
                "city": "Warsaw",
                "postal_code": "00-001",
                "country": "Poland",
            },
            "recipient": {
                "name": "John",
                "phone_number": "+48987654321",
                "address": {
                    "street_address": "Second Street 5",
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
        },
    )

    assert response.status_code == 422
