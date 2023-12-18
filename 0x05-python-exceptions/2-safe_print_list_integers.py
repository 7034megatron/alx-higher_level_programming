#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    result = []
    try:
        for i in range(x):
            print("{:d}".format(my_list[i]))
            result.append(my_list[i])
    except:
        pass
    return len(result)
