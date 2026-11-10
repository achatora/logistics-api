from dataclasses import dataclass, field
from datetime import UTC, datetime
from decimal import Decimal
from uuid import UUID, uuid4

from app.common.address import Address
from app.shipment.item import Item
from app.shipment.recipient import Recipient
from app.shipment.shipment_status import ShipmentStatus


# empty string validator
def empty_str_validator(value: str, field_name: str) -> None:
    if value is None or not value.strip():
        raise ValueError(f"{field_name} cannot be empty")


@dataclass
class Shipment:
    customer_id: int
    sender_name: str
    sender_phone_number: str
    sender_email: str
    sender_address: Address
    recipient: Recipient
    items: list[Item]
    shipment_id: UUID = field(default_factory=uuid4)
    status: ShipmentStatus = ShipmentStatus.PENDING
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    @property
    def total_weight(self) -> Decimal:
        return sum(
            (item.total_weight for item in self.items),
            Decimal(0),
        )

    def __post_init__(self) -> None:
        if self.customer_id is None:
            raise ValueError("Customer ID cannot be empty")

        empty_str_validator(self.sender_name, "Sender name")
        empty_str_validator(self.sender_phone_number, "Sender phone number")
        empty_str_validator(self.sender_email, "Sender email")

        if self.sender_address is None:
            raise ValueError("Sender address cannot be empty")

        if self.recipient is None:
            raise ValueError("Recipient cannot be empty")

        if not self.items:
            raise ValueError("Items cannot be empty")
