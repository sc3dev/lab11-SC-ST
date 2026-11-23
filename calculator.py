# https://github.com/sc3dev/lab11-SC-ST
# Partner 1: Sullivan Christ
# Partner 2: Sullivan Christ
from math import log, sqrt, hypot
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def logarithm(a, b):
    if a < 0 or a == 1 or b < 0:
        raise ValueError
    return log(b, a)

def exp(a, b):
    return a**b

def square_root(a):
    if a < 0:
        raise ValueError
    return sqrt(a)

def hypotenuse(a, b):
    return hypot(a, b)
