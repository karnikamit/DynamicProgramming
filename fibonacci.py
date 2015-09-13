__author__ = 'karnikamit'


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print fibo(10)  # 55

"""
Reducing the complexity from exponential to polynomial using Memorization
"""


fibTable = {1: 1, 2: 1}


def Fibo(n):
    if n in fibTable:
        return fibTable[n]
    else:
        fibTable[n] = Fibo(n-1) + Fibo(n-2)
        return fibTable[n]

print Fibo(10)