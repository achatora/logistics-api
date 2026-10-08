import pytest

from app.common.address import Address
from app.customer.customer import Customer


def test_customer_can_be_created():
    address = Address(
        "Brooklyn Rd",
        "San Francisco",
        "00-000",
        "USA",
    )

    customer = Customer(
        "Felix",
        "email@gmail.com",
        "123-456-789",
        address,
    )

    assert customer.name == "Felix"
    assert customer.email == "email@gmail.com"
    assert customer.phone_number == "123-456-789"
    assert customer.address == address
    assert customer.customer_id is None


def test_customer_rejects_empty_email():

    with pytest.raises(ValueError):
        address = Address(
            "Brooklyn Rd",
            "San Francisco",
            "00-000",
            "USA",
        )

        Customer(
            "Felix",
            "",
            "123-456-789",
            address,
        )


def test_customer_rejects_none_address():

    with pytest.raises(ValueError):
        Address(
            "Brooklyn Rd",
            "San Francisco",
            "00-000",
            "USA",
        )

        customer = Customer(
            "Felix",
            "email@gmail.com",
            "123-456-789",
            None,  # pyright: ignore[reportArgumentType]
        )

        assert customer.name == "Felix"
        assert customer.email == "email@gmail.com"
        assert customer.phone_number == "123-456-789"
        assert customer.address == None
        assert customer.customer_id is None
