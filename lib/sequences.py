#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    for i in range(length):
        if i < 2:
            fib.append(i)
        else:
            new_num = fib[len(fib)-1] + fib[len(fib)-2]
            fib.append(new_num)
    print(fib)
    
# print_fibonacci(0)