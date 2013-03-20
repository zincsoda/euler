#!/usr/bin/python

import math

def is_prime(number):
    """Returns true if number is a prime"""
    if number == 1: return False
    if number == 2: return True
    if number == 3: return True
    if number == 5: return True
    if number == 7: return True
    if number % 2 == 0: return False
    if number % 3 == 0: return False
    k, a, b = 1, 0, 0
    sr = int(math.sqrt(number))
    while b < sr:
        a = (6 * k) - 1
        b = (6 * k) + 1
        if number % a == 0:
            return False
        if number % b == 0:
            return False
        k += 1
    return True
	
	
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm"""
    while b:
       a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple"""
    return (a * b) / (gcd(a, b))

def lcmm(*args):
    """Return lcm of args"""
    return reduce(lcm, args)

        
def get_n_primes(n):
    primes = []
    i = 1
    while len(primes) <= n:
        if is_prime(i): primes.append(i)
        i+=1
    return primes


def get_prime_factors(n):
    r = n
    prime_factors = []
    p = 2
    while p*p <= r:
        if r % p == 0:
            prime_factors.append(p)
            r = r / p
        else:
            p+=1
    prime_factors.append(r)
    return prime_factors 


def number_of_divisors(prime_factors):
    nod = 1
    for uniq_pf in set(prime_factors):
        nod = nod * (prime_factors.count(uniq_pf)+1)
    return nod

if __name__=="__main__":
    get_prime_factors(225)
