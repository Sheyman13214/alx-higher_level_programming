#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return []  # Return an empty list if my_list is not provided

    new_list = []

    for x in my_list:
        if x % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return (new_list)
