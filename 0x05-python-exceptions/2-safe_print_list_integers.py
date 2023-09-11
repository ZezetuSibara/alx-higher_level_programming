#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the 1st elements that are integers.

    Args:
        my_list (list): The list to print elements.
        x (int): The number of elements to print.

    Returns:
        The printed number of elements.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
