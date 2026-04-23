def validate_non_negative(value):
    if value < 0:
        raise ValueError("Negative values not allowed")
