__author__ = 'karnikamit'

# Finding the factorial of a given number

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print fact(10)

# Using table
factTable = {}
def factorial(n):
    try:
        return factTable[n]
    except KeyError:
        if n == 0:
            factTable[n] = 1
            return 1
        else:
            factTable[n] = n * factorial(n-1)
        return factTable[n]

print factorial(10)