#!/usr/bin/python2.6

from primes import get_prime_factors, number_of_divisors, get_n_primes
import math

def num_of_divisors(number):
    nod = 0
    sqrt = int(math.sqrt(number))
    for i in range(1,sqrt):
        if number % i == 0:
            nod += 2
    if (sqrt * sqrt == number):
        nod -= 1
    return nod


if __name__=="__main__":
    number = 0
    i = 1   
    while number_of_divisors(get_prime_factors(number)) < 500:
        #if i % 1000 == 0: print i, number
        number += i
        i +=1

    print number
