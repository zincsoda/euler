#!/usr/bin/python2.6

from math import factorial as f

def binomial_coef(n, r):
    return f(n) / (f(n-r) * f(r) )

if __name__=="__main__":
    """
    From the top left, to the bottom right, there is a choice at every next point to go horizontally or vertically.
    The is a binary choice so it could be represented as a 0 or 1. 
    The final solution would be a 40 digit binary number with 20 0's and 20 1's. This can be represented in 40 C 20 ways.
    """
    print "Solution = ", binomial_coef(40, 20)
