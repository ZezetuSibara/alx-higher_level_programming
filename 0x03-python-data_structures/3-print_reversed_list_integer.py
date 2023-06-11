#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Prints all numbers in reverse order."""
    if isinstance(my_list, list):
        my_list.reverse()
        for ii in my_list:
            print("{:d}".format(ii))
