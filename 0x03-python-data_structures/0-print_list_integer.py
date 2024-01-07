#!/usr/bin/python3

def print_list_integer(my_list=[]):
    if not my_list:  # Check if the list is empty
        return
    else:
        for i in my_list:
            print("{:d}".format(i))
