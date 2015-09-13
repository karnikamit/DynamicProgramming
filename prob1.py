__author__ = 'karnikamit'


def prob(n):
    T = [0] * (n+1)
    T[0] = T[1] = 2
    T[2] = 2 * T[1] * T[0]
    for i in xrange(1, n+1):
        T[i] = T[i-1] + 2 * T[i-1] * T[i-2]
    return T[n]

print prob(4)