#!/usr/bin/python
def rec_permute(sofar, rest):
    if rest == "":
        print 'sofar:', sofar
    else:
        for i in range(len(rest)):
            next = sofar + rest[i]
            print 'next = ', next
            remaining = rest[0:i] + rest[i+1:]
            print 'remaining = ', remaining
            print 'calling rec_permute(',next,',',remaining,')'
            rec_permute(next, remaining)
            print '---recursion---'

if __name__=='__main__':
    rec_permute('','abcd')
