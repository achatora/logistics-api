import pytest

from app.common.address import Address
from app.customer.customer_address import CustomerAddress


@pytest.fixture
def valid_address():
    return Address(
        street_address="10 Main Street",
        city="Warsaw",
        postal_code="00-001",
        country="Poland",
    )


def test_customer_address_can_be_created(valid_address):
    address = CustomerAddress(
        label="Home",
        address=valid_address,
    )

    assert address.label == "Home"
    assert address.address == valid_address


def test_customer_address_is_default_false_by_default(valid_address):
    address = CustomerAddress(label="Home", address=valid_address)

    assert address.is_default is False
    assert address.address_id is None
    assert address.customer_id is None
    assert address.created_at is None
    assert address.updated_at is None


def test_customer_address_rejects_empty_label(valid_address):
    with pytest.raises(ValueError, match="Label cannot be empty"):
        CustomerAddress(label="", address=valid_address)


def test_customer_address_rejects_blank_label(valid_address):
    with pytest.raises(ValueError, match="Label cannot be empty"):
        CustomerAddress(label="   ", address=valid_address)


def test_customer_address_rejects_none_address():
    with pytest.raises(ValueError, match="Address cannot be empty"):
        CustomerAddress(label="Home", address=None)  # pyright: ignore[reportArgumentType]
