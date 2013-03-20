#!/usr/bin/python2.6

def square_of_sum(n):
	return (n * n)*((n*n)+(2*n) + 1) / 4

def sum_of_squares(n):
	return (n * (n+1) * (2 * n + 1))/6

if __name__=="__main__":
    square_of_sum(100) - sum_of_squares(100)
