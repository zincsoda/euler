#!/usr/bin/python2.6

largest = 999 * 999

palins = []
i = largest
while len(palins) < 150:
    s = str(i)
    if s[0] == s[-1] and s[1] == s[-2] and s[2] == s[-3]:
        palins.append(i)
    i -= 1

print "Got first 150 palindromes"

for p in palins:
    print "Testing ", p
    n = 999
    while len(str(p/n)) == 3:
        if p % n == 0:
            print "%d x %d = %d" % (n, p/n, p)
            exit(0)
        n -= 1
    print "stopped looping at n = ", n

    
