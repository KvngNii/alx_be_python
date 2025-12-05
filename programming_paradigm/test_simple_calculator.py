import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Tests for Addition
    def test_addition(self):
        """Test the addition method with positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_addition_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_addition_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_addition_floats(self):
        """Test addition with floating point numbers."""
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(self.calc.add(-1.5, 1.5), 0.0)

    # Tests for Subtraction
    def test_subtraction(self):
        """Test the subtraction method with positive numbers."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)
        self.assertEqual(self.calc.subtract(100, 50), 50)

    def test_subtraction_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_subtraction_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtraction_floats(self):
        """Test subtraction with floating point numbers."""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.subtract(10.7, 5.2), 5.5)
        self.assertAlmostEqual(self.calc.subtract(0.5, 0.3), 0.2)

    def test_subtraction_result_negative(self):
        """Test subtraction resulting in negative numbers."""
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(10, 20), -10)

    # Tests for Multiplication
    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)
    
    def test_multiplication(self):
        """Test the multiplication method with positive numbers."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)
        self.assertEqual(self.calc.multiply(10, 10), 100)

    def test_multiplication_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-5, -4), 20)
        self.assertEqual(self.calc.multiply(5, -3), -15)

    def test_multiplication_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiplication_by_one(self):
        """Test multiplication by one."""
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, 5), 5)
        self.assertEqual(self.calc.multiply(-7, 1), -7)

    def test_multiplication_floats(self):
        """Test multiplication with floating point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 2.5), 3.75)
        self.assertAlmostEqual(self.calc.multiply(0.5, 0.5), 0.25)

    # Tests for Division
    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(20, 4), 5)
    
    def test_division(self):
        """Test the division method with positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(20, 4), 5)
        self.assertEqual(self.calc.divide(100, 10), 10)

    def test_division_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-20, -4), 5)
        self.assertEqual(self.calc.divide(15, -3), -5)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

    def test_division_zero_numerator(self):
        """Test division of zero by a non-zero number."""
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -3), 0)
        self.assertEqual(self.calc.divide(0, 100), 0)

    def test_division_floats(self):
        """Test division with floating point numbers."""
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(10.0, 4.0), 2.5)
        self.assertAlmostEqual(self.calc.divide(1.0, 3.0), 0.3333333333333333)

    def test_division_result_float(self):
        """Test division that results in floating point numbers."""
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5)
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.3333333333333335)
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25)

    def test_division_by_one(self):
        """Test division by one."""
        self.assertEqual(self.calc.divide(5, 1), 5)
        self.assertEqual(self.calc.divide(-10, 1), -10)
        self.assertEqual(self.calc.divide(0, 1), 0)

if __name__ == '__main__':
    unittest.main()
