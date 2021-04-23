""" @package parser
@brief Calculator input parser
@author Tadeas Vintrlik <xvintr04>

A very simple parser that serves
as an interface between the ::gui and ::math_library
"""

OPERATORS = ["√", "+", "-", "*", "/", "^", "!", "Fib"]

def check_valid(text):
    """ @brief check if a valid (computable) input
    @param text input from the calculator entry
    """
    op_count = 0  # Number of operators
    for char in text:
        if char in OPERATORS:
            op_count += 1
    return op_count == 1
