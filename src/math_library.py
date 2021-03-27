## @package math_library
#  Author: Vojtech Fiala <xfiala61>
#  Documentation for this module.
#

def convert_reverse(number, system):
    return True

def convert(number, system, acc=5):
    return True

def factorial(number):
    if number < 0 or isinstance(number, float):
        raise ValueError

    result = 1
    for i in range(0, number):
        result *= number
        number -= 1
    return result

def add(number, number2):
    return True

def sub(number, number2):
    return number - number2

def multiply(number, number2):
    return number * number2

def divide(number, number2):
    return number / number2

def exp(number, number2):
    if number2 < 0:
        raise ValueError
    return pow(number, number2)

def sqrt(number, number2):
    if number < 0:
        raise ValueError
    return pow(number, 1/number2)
