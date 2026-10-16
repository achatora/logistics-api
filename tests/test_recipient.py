import pytest

from app.common.address import Address
from app.shipment.recipient import Recipient


def test_recipient_can_be_created():

    address = Address("1234 Street", "Sydney", "123456", "Australia")

    recipient = Recipient("John", "123-456-789", address)

    assert recipient.name == "John"
    assert recipient.phone_number == "123-456-789"
    assert recipient.address == address


def test_recipient_rejects_none_address():

    with pytest.raises(ValueError):
        Recipient(
            "John",
            "1234-456-789",
            None,  # pyright: ignore[reportArgumentType]
        )


def test_recipient_rejects_empty_name():

    address = Address("1234 Street", "Sydney", "123456", "Australia")

    with pytest.raises(ValueError):
        Recipient(
            "",
            "1234-456-789",
            address,
        )
