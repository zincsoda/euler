#!/usr/bin/python2.6

def nums():
    result = []
    for x in range(1000):
        if x % 3 == 0:
            result.append(x)
        elif x % 5 == 0:
            result.append(x)
    return result
            

if __name__=="__main__":
    sum = 0
    for x in nums():
        sum = sum + x
    print sum
