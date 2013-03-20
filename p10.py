#!/usr/bin/python2.6

from pylib.primes import is_prime

if __name__=="__main__":
    l = 2000000
    sum = 0
    for i in range(l):
        if is_prime(i):
            sum += i
    print sum
