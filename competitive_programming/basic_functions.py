# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from functools import reduce
def func (x, y):
    print(x+y)

def passfunc():
    print("pass")
    pass

def factorial (n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
def args(*args):
    return sum(args)
    
def kwargs(**kwargs):
    sum=0
    for k, val in kwargs.items():
        sum+=val
    return sum
