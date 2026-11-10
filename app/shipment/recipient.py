from dataclasses import dataclass

from app.common.address import Address
from app.common.validators import empty_str_validator


@dataclass
class Recipient:
    name: str
    phone_number: str
    address: Address

    def __post_init__(self) -> None:

        empty_str_validator(self.name, "Name")
        empty_str_validator(self.phone_number, "Phone number")

        if self.address is None:
            raise ValueError("Address cannot be empty")
