#!/usr/bin/python3
def print_last_digit(number):
    a = 0
    if number < 0:
        number *= -1
        a = 1
    last_digit = number % 10
    if a == 1:
        number *= -1
    print("{:d}".format(last_digit), end="")
    return last_digit
