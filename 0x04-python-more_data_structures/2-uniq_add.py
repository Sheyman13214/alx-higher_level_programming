#!/usr/bin/python3

def uniq_add(my_list=[]):
    if not my_list:
        return None
    unique_int = set()  # Create a set to store unique integers
    total = 0  # Initialize the total to 0
    for num in my_list:
        if isinstance(num, int):
            if num not in unique_int:
                total += num
                unique_int.add(num)
    return total
