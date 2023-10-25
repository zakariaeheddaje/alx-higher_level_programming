#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError('Too far')  # Specify the exception type
            else:
                result += a ** b / i
        except ValueError:  # Catch the specific exception
            result = b + a
            break
    return result
