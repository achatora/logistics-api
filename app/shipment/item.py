from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Item:
    name: str
    weight: Decimal
    quantity: int

    def __post_init__(self) -> None:
        if self.name is None or not self.name.strip():
            raise ValueError("Item name cannot be empty")

        if self.weight is None or self.weight <= Decimal(0):
            raise ValueError("Weight must be greater than zero")

        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

    @property
    def total_weight(self) -> Decimal:
        return self.weight * self.quantity
