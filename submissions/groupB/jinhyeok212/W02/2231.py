# 2231번: 분해합 - 브루트포스 범위 계산

import sys

input = sys.stdin.readline
n = int(input().strip())

answer = 0

for i in range(1, n+1): # 1부터 입력값 + 1까지
    num = sum(map(int, str(i))) # i의 각 자리수 합 계산 

    if i + num == n:  # i + 자리수 합 = 입력값 이면 answer에 저장
        answer = i
        break

print(answer)