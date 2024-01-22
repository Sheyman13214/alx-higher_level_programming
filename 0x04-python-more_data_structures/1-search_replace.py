#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if not my_list:
        return None
    new_list = my_list[:]  # create a copy of the list
    if search in new_list:
        for i in range(len(new_list)):
            if new_list[i] == search:
                new_list[i] = replace
    return new_list
