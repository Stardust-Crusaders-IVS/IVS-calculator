""" @package profiling
    @author: Vojtech Bubela <xbubel08>
    @brief prifiling file
"""
import sys
from math_library import add, sub, multiply, divide
from math_library import exp, sqrt, fibonacci

# pomocne funkce

def load_input():
    my_list = []

    for line in sys.stdin:
        x = line.rstrip()
        if x == '':
            break
        else:   
            my_list.append(x)

    return my_list
        

def arithmetic(my_list):
    result = 0;
    for number in my_list:
        result = add(result, int (number))

    return divide(result,len(my_list))
# promene

final_result = None;


def main():
    my_list = load_input()
    
    arithm = arithmetic(my_list)

    square_arithm = exp(arithm, 2)

    sum_result = 0
    resulto = 0

    for number in my_list:
        x = exp(int (number), 2)
        resulto = add(x, resulto)

    resultino = sub(resulto, multiply(len(my_list), square_arithm))

    more_result = divide(resultino, sub(len(my_list), 1))

    final_result = sqrt(more_result, 2)

    print(final_result)


if __name__ == '__main__':
    main()
