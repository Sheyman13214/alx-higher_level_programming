#!/usr/bin/python3
def no_c(my_string):
    if not my_string:  # Check if the input string is empty
        return my_string  # Return the empty string as-is
    new_str_list = []
    for x in my_string:
        if x != 'c' and x != 'C':
            new_str_list.append(x)  # Append characters to the list
    new_str = ''.join(new_str_list)  # Join the list into a single string
    return (new_str)
