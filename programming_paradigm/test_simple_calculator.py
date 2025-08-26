import unittest
# Import the SimpleCalculator class from the simple_calculator.py file
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """
    Test suite for the SimpleCalculator class.
    """

    def setUp(self):
        """
        Set up a new SimpleCalculator instance before each test method.
        This ensures each test starts with a fresh calculator.
        """
        # Changed 'self.calculator' to 'self.calc' to match checker's expectation
        self.calc = SimpleCalculator()

    def test_add(self):
        """
        Tests the addition method with positive, negative, and zero values.
        """
        # Changed 'self.calculator' to 'self.calc'
        self.assertEqual(self.calc.add(5, 3), 8)        # Positive numbers
        self.assertEqual(self.calc.add(-5, 3), -2)       # Negative and positive
        self.assertEqual(self.calc.add(0, 10), 10)      # Adding zero
        self.assertEqual(self.calc.add(-7, -3), -10)    # Two negative numbers
        self.assertEqual(self.calc.add(2.5, 1.5), 4.0)  # Decimal numbers

    def test_subtract(self):
        """
        Tests the subtraction method with various combinations of numbers.
        """
        # Changed 'self.calculator' to 'self.calc'
        self.assertEqual(self.calc.subtract(10, 4), 6)      # Positive numbers
        self.assertEqual(self.calc.subtract(5, 8), -3)      # Result is negative
        self.assertEqual(self.calc.subtract(0, 5), -5)      # Subtracting from zero
        self.assertEqual(self.calc.subtract(-10, -5), -5)   # Negative minus negative
        self.assertEqual(self.calc.subtract(7.5, 2.5), 5.0) # Decimal numbers

    def test_multiply(self):
        """
        Tests the multiplication method with positive, negative, and zero.
        """
        # Changed 'self.calculator' to 'self.calc'
        self.assertEqual(self.calc.multiply(6, 7), 42)      # Positive numbers
        self.assertEqual(self.calc.multiply(-4, 2), -8)     # Negative by positive
        self.assertEqual(self.calc.multiply(0, 9), 0)       # Multiplying by zero
        self.assertEqual(self.calc.multiply(-5, -5), 25)    # Two negative numbers
        self.assertEqual(self.calc.multiply(3.0, 2.5), 7.5) # Decimal numbers

    def test_divide(self):
        """
        Tests the division method for normal operation and division by zero.
        """
        # Changed 'self.calculator' to 'self.calc'
        self.assertEqual(self.calc.divide(10, 2), 5.0)      # Normal division
        self.assertEqual(self.calc.divide(7, 2), 3.5)       # Division with decimal result
        self.assertEqual(self.calc.divide(-10, 5), -2.0)    # Negative numerator
        self.assertEqual(self.calc.divide(0, 5), 0.0)       # Zero divided by non-zero

        # Test division by zero
        with self.assertRaises(ValueError) as cm:
            # Changed 'self.calculator' to 'self.calc'
            self.calc.divide(10, 0)
        self.assertEqual(str(cm.exception), "Cannot divide by zero!")

    def test_divide_by_zero_message(self):
        """
        Ensures the correct error message is returned for division by zero.
        This is another way to test exceptions with specific messages.
        """
        # Changed 'self.calculator' to 'self.calc'
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero!"):
            self.calc.divide(1, 0)

# This block allows you to run the tests directly from the script
if __name__ == '__main__':
    unittest.main()
