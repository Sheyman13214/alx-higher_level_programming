#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    # Find elements that are in set_1 but not in set_2
    only_in_set_1 = set_1 - set_2

    # Find elements that are in set_2 but not in set_1
    only_in_set_2 = set_2 - set_1

    # Combine the two sets to get elements that are only in one of the sets
    result = only_in_set_1.union(only_in_set_2)

    return result
