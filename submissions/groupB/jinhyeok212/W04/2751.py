# 수 정렬하기 2

import sys
input=sys.stdin.readline

n = int(input())
list = []

for _ in range(n):
    list.append(int(input()))

list.sort() # 오름차순 정렬

for i in list:
    print(i)