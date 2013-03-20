#!/usr/bin/python2.6

if __name__=="__main__":
    number_string = str(2 ** 1000)
    sum = 0
    for i in range(len(number_string)):
        sum += int(number_string[i])
    print sum
