#!/usr/bin/python3

def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except:
        pass
    finally:
        if result is not None:
            print("{}".format())
    return None

