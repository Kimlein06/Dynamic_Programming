# using recurrsion : dynamic programing
from datetime import datetime as dt
start = dt.now().microsecond
def fib(n):
    if n == 0:
        result = 0
    elif n == 1 or n == 2:
        result = 1
    else:
        result =  fib(n-1) + fib(n-2)
    return result

print(fib(10))
print(f"Time taken by recursion: {dt.now().microsecond - start} microseconds")