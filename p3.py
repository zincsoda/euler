#!/usr/bin/python2.6

from pylib.primes import get_prime_factors

if __name__=="__main__":
    n = 600851475143
    print max(get_prime_factors(n))
