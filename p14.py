#!/usr/bin/python2.6

def collatz_list(n):
    l = []
    r = n
    l.append(r)
    while r > 1:
        if r % 2 == 0:
            r = r/2
        else:
            r = 3*r + 1
        l.append(r) 
    return l


if __name__=="__main__":
    starting_number = 1
    chain_length = 1
    for i in range(500001,1000001):
        cl = collatz_list(i)
        l = len(cl)
        if l > chain_length:
            print i,l
            chain_length = l
            starting_number = i

    print starting_number, chain_length
