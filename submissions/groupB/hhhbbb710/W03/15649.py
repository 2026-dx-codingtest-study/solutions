from itertools import permutations, combinations
import sys

input = sys.stdin.readline
num = input().split()

N, M = int(num[0]), int(num[1])
result = permutations(range(1, N+1), M)  # 순열의 결과를 result에 저장

for i in result:  # result에 들어있는 결과를 다 풀어서 출력
  print(*i)