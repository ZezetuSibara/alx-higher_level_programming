#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Search the biggest number of a list."""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for ii in range(len(my_list)):
        if my_list[ii] > big:
            big = my_list[ii]

    return (big)
