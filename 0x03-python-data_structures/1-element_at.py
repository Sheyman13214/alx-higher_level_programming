#!/usr/bin/python3

def element_at(my_list, idx):
    if not my_list:  # Check if the list is empty
        return None
    elif idx < 0 or idx >= len(my_list):
        return None
    else:
        return my_list[idx]
