from dataclasses import dataclass
from datetime import datetime


# None and empty string validation
def str_validation_check(text: str, field_name: str) -> None:
    if text is None or not text.strip():
        raise ValueError(f"{field_name} cannot be empty")


@dataclass
class Customer:
    first_name: str
    last_name: str
    phone_number: str
    customer_id: int | None = None
    user_id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __post_init__(self) -> None:

        str_validation_check(self.first_name, "Name")
        str_validation_check(self.last_name, "Last name")
        str_validation_check(self.phone_number, "Phone number")
