#!/usr/bin/python2.6

import math

if __name__=="__main__":
    f = math.factorial(100)
    sum = 0
    for i in str(f):
        sum += int(i)
    print sum
