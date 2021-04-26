""" @package math_library
    @author: Vojtech Fiala <xfiala61>
    @brief Documentation for math library.
"""

###################################################
#              Custom Exception                   #
###################################################

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

###################################################
#         Convertor inner functionality           #
###################################################

def get_dec_result(dec_part, system):
    """ @brief Convert the decimal part of a given number to decimal system.
        @param dec_part The decimal part to convert.
        @param system Can be any system from 2-16.
    """
    result = 0
    length = len(dec_part)

    while length > 0:
        result += (convert_to_dec(dec_part[length-1], system) * (pow(system, -length)))
        length -= 1

    return result

def get_norm_result(number, system):
    """ @brief Convert the integer part of a given number to decimal system.
        @param number The number part to convert.
        @param system Can be any system from 2-16.
    """
    result = 0
    length = len(number)
    i = 0

    while length > 0:
        result += (convert_to_dec(number[-1-i], system) * (pow(system, i)))
        i += 1
        length -= 1
    return result

def convert_to_dec(letter, system):
    """ @brief Convert number from string to integer.
        If the remain is from a system > 10, convert it to decimal.
        @param letter The letter representing the number to convert.
        @param system Can be anything from 2-16.
    """
    ret = 0
    if letter == 'A':
        ret = 10
    elif letter == 'B':
        ret = 11
    elif letter == 'C':
        ret = 12
    elif letter == 'D':
        ret = 13
    elif letter == 'E':
        ret = 14
    elif letter == 'F':
        ret = 15
    else:
        try:
            ret = int(letter)
        except:
            raise InvalidSystem

    if ret >= system:
        raise InvalidSystem
    return ret


def convert_to_system(number):
    """ @brief Convert number from integer to string.
        If the number is >= 10, change its representation.
        @param number The number to convert.
    """
    if number >= 10:  # If it's less than 10, there's no need to do anything
        number = str(number)
        if number == '10':
            number = 'A'
        elif number == '11':
            number = 'B'
        elif number == '12':
            number = 'C'
        elif number == '13':
            number = 'D'
        elif number == '14':
            number = 'E'
        elif number == '15':
            number = 'F'
        else:
            raise InvalidSystem

    return number

def convert_int(number, system):
    """ @brief Convert the integer part of a number.
        @param number The number to convert.
        @param system Can be any system from 2-16.
    """
    arr = []
    number = int(number)  # Get rid of the decimal part

    if number == 0:  # If it's zero, just append it
        arr.append(number)

    while number != 0:

        remain = number % system
        remain = convert_to_system(remain)
        arr.append(remain)
        number = int(number / system)

    new_arr = []
    i = len(arr)

    while i > 0:  # Revert the result (Highest value is the left one)
        new_arr.append(arr[i-1])
        i -= 1

    return new_arr

def convert_dec(number, system, acc):
    """ @brief Convert the decimal part of a number.
        @param number The number to convert.
        @param acc The accuracy of the result.
    """
    dec_rem = []

    if isinstance(number, float):  # Check if there actually is a decimal part

        dec_rem.append('.')
        dec = number-int(number)
        sub_zero_remain = dec

        while len(dec_rem) <= acc: # Go until I have reached the desired acc

            sub_zero_remain = (sub_zero_remain * system)

            app = int(sub_zero_remain % system)
            app = convert_to_system(app)
            dec_rem.append(app)

            if sub_zero_remain >= (system-1):
                sub_zero_remain = sub_zero_remain - (system-1)

    return dec_rem

###################################################
#              Convertor functions                #
###################################################

def convert_reverse(number, system):
    """ @brief Convert number from given system to decimal.
        @param number The number to convert.
        @param system Can be any system from 2-16.
    """
    dot = -1
    number = str(number)

    for i in range(0, len(number)):
        if number[i] == '.':
            dot = i
            break

    if dot > 0:
        dec_part = number[dot+1:]
        norm_part = number[:dot]


        dot_part = get_dec_result(dec_part, system)
        full = get_norm_result(norm_part, system)

    else:
        dot_part = 0
        full = get_norm_result(number, system)

    return dot_part + full


def convert(number, system, acc=5):
    """ @brief Convert number from decimal to given system.
        @param number The number to convert.
        @param system Can be any system from 2-16.
        @param acc Accuracy used to count decimal parts. Defaults to 5.
    """
    int_part = convert_int(number, system)
    dec_part = convert_dec(number, system, acc)

    result = int_part + dec_part


    ret = ''
    for part in result:
        ret += str(part)

    if ret[-1] == '.':
        ret = ret[:-1]

    return ret

###################################################
#              Math Functions                     #
###################################################

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
