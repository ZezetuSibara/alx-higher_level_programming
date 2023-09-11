#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    """Safely executes the function.

    Args:
        fct: The actual function needing to be execute.
        args: Arguments used for fct.

    Returns:
        Should an error occurs - None.
        Else - the result of the call to fct.
    """
    try:
        f = fct(*args)
        return (f)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        return None
