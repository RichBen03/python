class InvalidInputError(Exception):
    """Custom exception for invalid inputs that can't be processed."""
    pass

class ComplexCalculator:
    def __init__(self):
        pass

    def _convert_to_number(self, value):
        """Attempts to convert a value to an appropriate numeric type."""
        try:
            # Check if the value is a complex number
            if isinstance(value, complex):
                return value
            # Try converting to an integer first
            if '.' not in str(value):
                return int(value)
            # Try converting to a float if there's a decimal point
            return float(value)
        except ValueError:
            raise InvalidInputError(f"Invalid input: '{value}' cannot be converted to a number.")