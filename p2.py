#!/usr/bin/python2.6

def sum_fib():
    x = 1
    y = 2
    sum = 0
    while y < 4000000:
        if y % 2 == 0:
            sum = sum + y
        tmp = x + y
        x = y
        y = tmp
    return sum    

if __name__ == "__main__":
    print sum_fib()
