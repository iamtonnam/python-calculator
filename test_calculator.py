import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    # Tests for add()
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    # Tests for subtract()
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 10), 5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-2, -5), -3)

    # Tests for multiply()
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)

    # Tests for divide()
    def test_divide_even_division(self):
        self.assertEqual(self.calc.divide(10, 2), 1)

    def test_divide_uneven_division(self):
        self.assertEqual(self.calc.divide(9, 2), 1)  

    # Tests for modulo()
    def test_modulo_positive_numbers(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_no_remainder(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)


if __name__ == '__main__':
    unittest.main()