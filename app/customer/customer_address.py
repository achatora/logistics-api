from dataclasses import dataclass
from datetime import datetime

from app.common.address import Address
from app.common.validators import empty_str_validator


@dataclass
class CustomerAddress:
    label: str
    address: Address
    is_default: bool = False
    address_id: int | None = None
    customer_id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    def __post_init__(self) -> None:

        empty_str_validator(self.label, "Label")

        if self.address is None:
            raise ValueError("Address cannot be empty")
