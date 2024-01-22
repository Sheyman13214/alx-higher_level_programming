#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    # Check if my_list is not empty or None
    if my_list is not None:
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    count += 1
            except (ValueError, TypeError):
                pass
    print()
    return count
