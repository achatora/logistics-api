from dataclasses import dataclass, field
from datetime import UTC, datetime
from decimal import Decimal
from uuid import UUID, uuid4

from app.common.address import Address
from app.shipment.item import Item
from app.shipment.recipient import Recipient
from app.shipment.shipment_status import ShipmentStatus


@dataclass
class Shipment:
    sender_name: str
    sender_phone_number: str
    sender_address: Address
    recipient: Recipient
    items: list[Item]
    customer_id: int | None = None
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
        if self.sender_name is None or not self.sender_name.strip():
            raise ValueError("Sender name cannot be empty")

        if self.sender_phone_number is None or not self.sender_phone_number.strip():
            raise ValueError("Sender phone number cannot be empty")

        if self.sender_address is None:
            raise ValueError("Sender address cannot be empty")

        if self.recipient is None:
            raise ValueError("Recipient cannot be empty")

        if not self.items:
            raise ValueError("Items cannot be empty")
