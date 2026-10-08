from dataclasses import dataclass


@dataclass
class Address:
    street_address: str
    city: str
    postal_code: str
    country: str

    def __post_init__(self) -> None:
        # None or empty validation check
        def validation_check(text: str, field_name: str) -> None:
            if text is None or not text.strip():
                raise ValueError(f"{field_name} cannot be empty")

        validation_check(self.street_address, "Street address")
        validation_check(self.city, "City")
        validation_check(self.postal_code, "Postal code")
        validation_check(self.country, "Country")
