#!/usr/bin/python3
"""Module used to find the max integer
"""


def max_integer(list=[]):
    """This function  is used to find and return the max integer
        If the list is empty, the function returns Nothing
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
