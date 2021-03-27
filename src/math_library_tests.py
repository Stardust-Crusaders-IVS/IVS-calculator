""" @package math_library_tests
    @author: Vojtech Fiala <xfiala61>
Documentation for math library tests.
"""
import unittest
from math_library import add, sub, multiply, divide, InvalidSystem
from math_library import exp, sqrt, factorial, convert, convert_reverse

class TestStringMethods(unittest.TestCase):
    """ @brief Test class to run the tests.
        @param unittest.TestCase Used to get access to test methods.
    """

    def test_addition(self):
        """ @brief Method to test the addition (+).
            @param self Self object.
        """
        self.assertEqual(add(5, 5), 10)
        self.assertEqual(add(5, 15009), 15014)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, -5), -5)
        self.assertEqual(add(-5, 0), -5)
        self.assertEqual(add(-5, -5), -10)
        self.assertEqual(add(0.5, 5.8), 6.3)

    def test_substraction(self):
        """ @brief Method to test the substraction (-).
            @param self Self object.
        """
        self.assertEqual(sub(5, 5), 0)
        self.assertEqual(sub(5, 15009), -15004)
        self.assertEqual(sub(0, 0), 0)
        self.assertEqual(sub(0, -5), 5)
        self.assertEqual(sub(-5, 0), -5)
        self.assertEqual(sub(-5, -5), 0)
        self.assertEqual(sub(0.5, 5.8), -5.3)


    def test_multiplication(self):
        """ @brief Method to test the multiplication (*).
            @param self Self object.
        """
        self.assertEqual(multiply(5, 5), 25)
        self.assertEqual(multiply(5, 15009), 75045)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(0, -5), 0)
        self.assertEqual(multiply(-54654564, 0), 0)
        self.assertEqual(multiply(-5, -5), 25)
        self.assertEqual(multiply(-5, 5), -25)
        self.assertEqual(multiply(0.5, 5.8), 2.9)

    def test_division(self):
        """ @brief Method to test the division (/).
            @param self Self object.
        """
        self.assertEqual(divide(5, 5), 1)
        self.assertEqual(divide(5, 100), 0.05)
        self.assertRaises(ZeroDivisionError, divide, 0, 0)
        self.assertRaises(ZeroDivisionError, divide, -5, 0)
        self.assertEqual(divide(0, -5), 0)
        self.assertEqual(divide(-5, -5), 1)
        self.assertEqual(divide(-5, 5), -1)
        self.assertEqual(divide(8.5, 0.5), 17)

    def test_exp(self):
        """ @brief Method to test the exponent (^).
            @param self Self object.

        The exponent can only be a natural number, which includes 0.
        """
        self.assertEqual(exp(5, 5), 3125)
        self.assertEqual(exp(5, 2), 25)
        self.assertEqual(exp(0, 5), 0)
        self.assertEqual(exp(5, 0), 1)
        self.assertEqual(exp(-5, 5), -3125)
        self.assertRaises(ValueError, exp, 9, 0.5)
        self.assertEqual(exp(2, 31), 2147483648)
        self.assertRaises(ValueError, exp, 654, -5)

    def test_sqrt(self):
        """ @brief Method to test the root (√).
            @param self Self object.
        The root function doesn't support imaginary numbers.
        The operand must be a real number.
        This function supports n-th root. The 'n' can be any integer.
        """
        self.assertEqual(sqrt(9, 2), 3)
        self.assertEqual(sqrt(27, 3), 3)
        self.assertEqual(sqrt(0, 5), 0)
        self.assertEqual(sqrt(1, 5), 1)
        self.assertEqual(sqrt(1, -5), 1)
        self.assertRaises(ZeroDivisionError, sqrt, 5, 0)
        self.assertRaises(ValueError, sqrt, -5, 0)
        self.assertEqual(sqrt(5, -1), 0.2)
        self.assertEqual(sqrt(9, 1), 9)


    def test_fact(self):
        """ @brief Method to test the factorial (!)
            @param self Self object.
        Factorial operand can be any integer higher than 0.
        """
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertRaises(ValueError, factorial, -1)
        self.assertRaises(ValueError, factorial, 5.5)

    def test_convert(self):
        """ @brief Method to test the number system convertor.
            @param self Self object.
        Supports conversion from decimal system to any given system (2-16).
        Supports reverse conversion from any given system (2-16) to decimal.
        """
        self.assertEqual(convert(9, 2), "1001")
        self.assertEqual(convert(0, 2), "0")
        self.assertEqual(convert(16, 2), "10000")
        self.assertEqual(convert(16.5, 2, 5), "10000.10000")
        self.assertEqual(convert(16.5, 2), "10000.10000")
        self.assertEqual(convert(16.5, 2, 1), "10000.1")
        self.assertEqual(convert(16.5, 2, 0), "10000")
        self.assertEqual(convert(0.3, 2, 10), "0.0100110011")
        self.assertEqual(convert(4, 4), "10")
        self.assertEqual(convert(13, 16), "D")
        self.assertEqual(convert(57, 16), "39")
        self.assertEqual(convert(158, 16), "9E")
        self.assertEqual(convert(158.11, 16), "9E.1C28F")
        self.assertEqual(convert(158.11, 16, 10), "9E.1C28F5C28F")
        self.assertEqual(convert(158., 16, 5), "9E.00000")

        self.assertRaises(InvalidSystem, convert_reverse, 9, 2)
        self.assertRaises(InvalidSystem, convert_reverse, 'B', 10)
        self.assertRaises(InvalidSystem, convert_reverse, 'F', 13)
        self.assertRaises(InvalidSystem, convert_reverse, 'G', 13)
        self.assertRaises(InvalidSystem, convert_reverse, 'G', 13)
        self.assertEqual(convert_reverse(0.5, 10), 0.5)
        self.assertEqual(convert_reverse(.5, 10), 0.5)
        self.assertEqual(convert_reverse(4556, 10), 4556)
        self.assertEqual(convert_reverse(4556.0, 10), 4556)
        self.assertEqual(convert_reverse(4556., 10), 4556)
        self.assertEqual(
            convert_reverse(4556568465468, 10), 4556568465468)
        self.assertEqual(
            convert_reverse(6545618.654564561, 10), 6545618.654564561)
        self.assertEqual(convert_reverse('345A.85A', 16), 13402.52197265625)
        self.assertEqual(convert_reverse('345A.85A', 11), 4542.7761081893313298272)

if __name__ == '__main__':
    unittest.main()
