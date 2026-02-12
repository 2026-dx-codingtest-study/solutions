import sys
input = sys.stdin.readline

num = int(input())

def factorial(num):
    if num <= 1: # num이 1보다 작으면 1을 반환
        return 1
    return num * factorial(num-1) # num과 num-1값이 들어간 factorial 함수 곱을 반환 및 재귀 호출
print(factorial(num))
    