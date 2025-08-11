from datetime import datetime as dt
start = dt.now().microsecond
def fib_down_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = {}
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]

    return bottom_up[n]

print(fib_down_up(10))
print(f"The program took {dt.now().microsecond - start} microseconds to run")