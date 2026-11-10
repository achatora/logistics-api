import pytest

from app.customer.customer import Customer


def test_customer_can_be_created():
    customer = Customer(
        first_name="Felix",
        last_name="Kiptoo",
        phone_number="123-456-789",
    )

    assert customer.first_name == "Felix"
    assert customer.last_name == "Kiptoo"
    assert customer.phone_number == "123-456-789"
    assert customer.customer_id is None
    assert customer.user_id is None
    assert customer.created_at is None
    assert customer.updated_at is None


def test_customer_rejects_empty_first_name():
    with pytest.raises(ValueError, match="Name cannot be empty"):
        Customer(first_name="", last_name="Kiptoo", phone_number="123-456-789")


def test_customer_rejects_blank_last_name():
    with pytest.raises(ValueError, match="Last name cannot be empty"):
        Customer(first_name="Felix", last_name="   ", phone_number="123-456-789")


def test_customer_rejects_blank_phone_number():
    with pytest.raises(ValueError, match="Phone number cannot be empty"):
        Customer(first_name="Felix", last_name="Kiptoo", phone_number="   ")


def test_customer_accepts_populated_ids_and_timestamps():
    from datetime import datetime, timezone

    now = datetime.now(timezone.utc)
    customer = Customer(
        first_name="Felix",
        last_name="Kiptoo",
        phone_number="123-456-789",
        customer_id=1,
        user_id=42,
        created_at=now,
        updated_at=now,
    )

    assert customer.customer_id == 1
    assert customer.user_id == 42
    assert customer.created_at == now
    assert customer.updated_at == now

