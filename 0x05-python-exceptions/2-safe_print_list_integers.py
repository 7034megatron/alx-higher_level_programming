#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                count += 1
    except (IndexError, ValueError):
        pass  # Handle IndexError or ValueError by doing nothing
    finally:
        print()  # Add a newline after printing integers
    return count
