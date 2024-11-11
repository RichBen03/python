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
    def add(self, a, b):
        a = self._convert_to_number(a)
        b = self._convert_to_number(b)
        return a + b
    
    def subtract(self, a, b):
        a = self._convert_to_number(a)
        b = self._convert_to_number(b)
        return a - b
    
    def multiply(self, a, b):
        a = self._convert_to_number(a)
        b = self._convert_to_number(b)
        return a * b
    def divide(self, a, b):
        a = self._convert_to_number(a)
        b = self._convert_to_number(b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    
calculator = ComplexCalculator()

try:
    # Test with mixed data types
    print("Addition:", calculator.add("10", 5.5))   
    print("Subtraction:", calculator.subtract(10, "3"))   
    print("Multiplication:", calculator.multiply("2", 3))
    print("Division:", calculator.divide("10", "2.5"))  
    print("Complex Addition:", calculator.add(3 + 4j, 5)) 