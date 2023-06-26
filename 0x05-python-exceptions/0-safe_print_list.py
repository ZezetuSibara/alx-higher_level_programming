#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
 """Prints number of elememts from a list.

    Args:
        my_list (list): The actual list to print from.
        x (int): The number of elements to print.

    Returns:
        The number of printed elements.
    """
    r_num = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            r_num += 1
        except IndexError:
            break
    print()
    return r_num
