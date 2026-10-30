from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, Field, field_validator

from app.common.address import Address
from app.shipment.item import Item
from app.shipment.recipient import Recipient
from app.shipment.shipment import Shipment
from app.shipment.shipment_status import ShipmentStatus


# empty string validation check
def validate_non_empty_string(value: str) -> str:
    if not value.strip():
        raise ValueError("This field cannot be empty")
    return value


class AddressSchema(BaseModel):
    street_address: str
    city: str
    postal_code: str
    country: str

    @field_validator(
        "street_address",
        "city",
        "postal_code",
        "country",
    )
    @classmethod
    def validate_address_fields(cls, value: str) -> str:
        return validate_non_empty_string(value)


class RecipientSchema(BaseModel):
    name: str
    phone_number: str
    address: AddressSchema

    @field_validator(
        "name",
        "phone_number",
    )
    @classmethod
    def validate_recipient_fields(cls, value: str) -> str:
        return validate_non_empty_string(value)


class ItemSchema(BaseModel):
    name: str
    weight: Decimal = Field(gt=0)
    quantity: int = Field(gt=0)

    @field_validator(
        "name",
    )
    @classmethod
    def validate_item_fields(cls, value: str) -> str:
        return validate_non_empty_string(value)


class CreateShipmentRequest(BaseModel):
    sender_name: str
    sender_phone_number: str
    sender_address: AddressSchema
    recipient: RecipientSchema
    items: list[ItemSchema]

    @field_validator(
        "sender_name",
        "sender_phone_number",
    )
    @classmethod
    def validate_sender_fields(cls, value: str) -> str:
        return validate_non_empty_string(value)

    def convert_to_domain(self) -> Shipment:
        return Shipment(
            sender_name=self.sender_name,
            sender_phone_number=self.sender_phone_number,
            sender_address=Address(**self.sender_address.model_dump()),
            recipient=Recipient(
                name=self.recipient.name,
                phone_number=self.recipient.phone_number,
                address=Address(**self.recipient.address.model_dump()),
            ),
            items=[Item(**item.model_dump()) for item in self.items],
        )


class ShipmentResponse(BaseModel):
    model_config = {"from_attributes": True}

    shipment_id: UUID
    sender_name: str
    sender_phone_number: str
    sender_address: AddressSchema
    recipient: RecipientSchema
    items: list[ItemSchema]
    status: ShipmentStatus
    created_at: datetime
    total_weight: Decimal
