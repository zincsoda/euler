#!/usr/bin/python2.6

from pylib.primes import *

def brute_force():
    a = 1
    while True:
        if a % 20 == 0:
            if a % 19 == 0:
                if a % 18 == 0:
                    if a % 17 == 0:
                        if a % 16 == 0:
                            if a % 15 == 0:
                                if a % 14 == 0:
                                    if a % 13 == 0:
                                        if a % 12 == 0:
                                            if a % 11 == 0:
                                                print a
                                                exit(0)
        a += 1

def fast():
    print lcmm(11, 12,13,14,15,16,17,18,19,20)

if __name__=="__main__":
    fast()
