import sys

def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    return 1

n = int(sys.stdin.readline().strip())
print(factorial(n))
