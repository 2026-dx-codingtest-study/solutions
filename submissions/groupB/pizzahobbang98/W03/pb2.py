import sys

N = int(sys.stdin.readline())

def fivo(num):
    # 조건문 사용하여 (N>=2)를 표현
    if num == 0:
        return num
    if num == 1:
        return num
    return fivo(num-2) + fivo(num-1)

print(fivo(N))