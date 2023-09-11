
#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints elememts of a list.

    Args:
        my_list (list): The actual list to print from.
        x (int): The number of elements of my_list to print.

    Returns:
        The printed number of elements.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
