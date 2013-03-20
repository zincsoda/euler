#!/usr/bin/python2.6

"""
Find the 10001st prime
"""
from primes import is_prime

x = 1
p_count = 0
		
while True:
	if is_prime(x):
		p_count += 1
	if p_count == 10001:
		print '10001st prime = ', x
		exit(0)
	x += 1
