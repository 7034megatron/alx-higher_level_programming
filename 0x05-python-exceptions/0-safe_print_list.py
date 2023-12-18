#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    results = []
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end = "")
            int(my_list[i])
            count += 1
            result.append(my_list[i])

    except Exception:
        pass: 

    print() 
    return count
