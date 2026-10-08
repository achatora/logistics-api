import pytest

from app.common.address import Address


def test_address_can_be_created():

    address = Address(
        "Brooklyn Rd",
        "San Francisco",
        "00-000",
        "USA",
    )

    assert address.street_address == "Brooklyn Rd"
    assert address.city == "San Francisco"
    assert address.postal_code == "00-000"
    assert address.country == "USA"


def test_address_rejects_empty_city():

    with pytest.raises(ValueError):
        Address(
            "Brooklyn Rd",
            "",
            "00-000",
            "USA",
        )
