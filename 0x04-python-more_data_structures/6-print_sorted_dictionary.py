#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Get a sorted list of the dictionary's keys
    sorted_key = sorted(a_dictionary)

    for key in sorted_key:
        value = a_dictionary[key]

        # Check if the value is another dictionary
        if isinstance(value, dict):
            print(f"{key}: {{")
            print_sorted_dictionary(value)
            print("}")
        else:
            # If the value is not a dictionary, print it directly
            print(f"{key}: {value}")
