#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if not my_list:
        return None  # Return None to indicate that the list is missing
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
