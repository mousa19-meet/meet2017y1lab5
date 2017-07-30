"""def fib(n):
    x = 0
    for i in range (n+1):
     x = x + n
    return x
    print(x)
"""

def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
    
