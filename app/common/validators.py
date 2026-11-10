# empty string validator
def empty_str_validator(value: str, field_name: str) -> None:
    if value is None or not value.strip():
        raise ValueError(f"{field_name} cannot be empty")
