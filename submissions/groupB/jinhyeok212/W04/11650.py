# 좌표 정렬하기

import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort(key=lambda x: (x[0], x[1])) # x[0] 기준으로 정렬하고 같을 경우 x[1] 기준으로 정렬하기
for i in arr:
    print(i[0], i[1])
