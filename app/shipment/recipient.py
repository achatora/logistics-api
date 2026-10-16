from dataclasses import dataclass

from app.common.address import Address


@dataclass
class Recipient:
    name: str
    phone_number: str
    address: Address

    def __post_init__(self) -> None:

        def str_validation(text: str, field_name: str) -> None:
            if text is None or not text.strip():
                raise ValueError(f"{field_name} cannot be empty")

        str_validation(self.name, "Name")
        str_validation(self.phone_number, "Phone number")

        if self.address is None:
            raise ValueError("Address cannot be empty")
