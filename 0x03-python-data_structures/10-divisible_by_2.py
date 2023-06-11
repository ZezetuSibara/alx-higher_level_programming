#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Look for all multiples of 2 from the list."""
    multiples = []
    for ii in range(len(my_list)):
        if my_list[ii] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
