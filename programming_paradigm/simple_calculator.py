# simple_calculator.py

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
                return a / b
        
        if __name__ == "__main__":
            calc = SimpleCalculator()
            print("Add: 2 + 3 =", calc.add(2, 3))
            print("Subtract: 5 - 2 =", calc.subtract(5, 2))
            print("Multiply: 4 * 3 =", calc.multiply(4, 3))
            result = calc.divide(10, 0)
            if result is None:
                print("Divide: 10 / 0 = Error (division by zero)")
            else:
                print("Divide: 10 / 0 =", result)