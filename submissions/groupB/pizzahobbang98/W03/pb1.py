import sys

N = int(sys.stdin.readline())

def factorial(num):
    if num == 0:
        return 1  # 0!은 1
    
    return num * factorial(num - 1) # 여기서 num과 재귀 호출된 값을 곱해서 바로 리턴!

print(factorial(N))