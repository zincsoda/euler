#!/usr/bin/python2.6



if __name__=="__main__":
    """
    a2 + b2 = c2
    a = m2 - n2
    b = 2mn
    c = m2 + n2
    m2 - n2 + 2mn + m2 + n2 = 1000
    m(m+n) = 500
    """
    for m in range(1, 499):
        for n in range(2, 499):
            if n >= m:
                break
            p = m * ( m + n)
            if p > 500:
                break
            if p == 500:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                print 'a, b, c = ', a,b,c
                print 'a * b * c = ', a * b * c
