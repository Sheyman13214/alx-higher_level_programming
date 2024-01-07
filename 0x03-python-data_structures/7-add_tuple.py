#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or len(tuple_a) < 2:
        if tuple_a is None:
            tuple_a = (0, 0)
        elif len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)

    if tuple_b is None or len(tuple_b) < 2:
        if tuple_b is None:
            tuple_b = (0, 0)
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)

    add2_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return add2_tuple
