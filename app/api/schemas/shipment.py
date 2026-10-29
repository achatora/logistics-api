from decimal import Decimal

from pydantic import BaseModel, Field, field_validator


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


# describes full shipment data to be
# sent for shipment to be created
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
