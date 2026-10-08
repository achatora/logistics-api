from dataclasses import dataclass

from app.common.address import Address


@dataclass
class Customer:
    name: str
    email: str
    phone_number: str
    address: Address
    customer_id: int | None = None

    def __post_init__(self) -> None:

        # None and empty string validation
        def str_validation_check(text: str, field_name: str) -> None:
            if text is None or not text.strip():
                raise ValueError(f"{field_name} cannot be empty")

        str_validation_check(self.name, "Name")
        str_validation_check(self.email, "Email")
        str_validation_check(self.phone_number, "Phone number")

        if self.address is None:
            raise ValueError("Address cannot be empty")
