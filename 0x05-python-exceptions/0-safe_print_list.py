#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    result_count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            result_count += 1
    except IndexError:
        pass  # Handle IndexError by doing nothing
    finally:
        print()  # Add a newline after printing elements
    return result_count
