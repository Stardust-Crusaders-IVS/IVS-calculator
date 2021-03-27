""" @package math_library
    @author: Vojtech Fiala <xfiala61>
Documentation for math library.
"""

class Error(Exception):
    """ @brief Initialize custom error class.
        @param Exception To use with a custom exception.
    """
    pass

class InvalidSystem(Error):
    """ @brief Create custom exception.
        @param From the Error class.
    """
    pass

def convert_reverse(number, system):
    """ @brief Convert number from given system to decimal.
        @param number The number to convert.
        @param system Can be any system from 2-16.
    """
    return True

def convert(number, system, acc=5):
    """ @brief Convert number from decimal to given system.
        @param number The number to convert.
        @param system Can be any system from 2-16.
        @param acc Accuracy used to count decimal parts. Defaults to 5.
    """
    return True

def factorial(number):
    """ @brief Calculate factorial of a number.
        @param number The number of which factorial to calculate.
    """
    if number < 0 or isinstance(number, float):
        raise ValueError

    result = 1
    for i in range(1, number+1):
        result *= i

    return result

def add(number, number2):
    """ @brief Add two numbers.
        @param number Operand 1.
        @param number2 Operand 2.
    """
    return number + number2

def sub(number, number2):
    """ @brief Substract two numbers.
        @param number Operand 1.
        @param number2 Operand 2.
    """
    return number - number2

def multiply(number, number2):
    """ @brief Multiply two numbers.
        @param number Operand 1.
        @param number2 Operand 2.
    """
    return number * number2

def divide(number, number2):
    """ @brief Divide two numbers.
        @param number Operand 1.
        @param number2 Operand 2.
    """
    return number / number2

def exp(number, number2):
    """ @brief Calculate exponent value of a number.
        @param number Base number.
        @param number2 The exponent.
    The base number must be a positive integer or 0.
    """
    if number2 < 0 or isinstance(number2, float):
        raise ValueError
    return pow(number, number2)

def sqrt(number, number2):
    """ @brief Calculate root value of a number.
        @param number Base number.
        @param number2 The n-th root.
    The base number must be a positive integer or 0.
    """
    if number < 0 or isinstance(number2, float):
        raise ValueError
    return pow(number, 1/number2)
