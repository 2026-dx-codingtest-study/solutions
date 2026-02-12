import sys
input = sys.stdin.readline

n = int(input())

def fibo(n):
    if n <= 1: # 입력값이 1보다 작거나 같을 때 n을 반환
        return n
    return fibo(n-1) + fibo(n-2) # fibo함수에 (n-2), (n-1)을 넣은 값을 반환 및 재귀 호출 

print(fibo(n))
