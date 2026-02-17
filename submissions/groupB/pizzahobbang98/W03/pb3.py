import sys
from itertools import permutations

# 입력 받기
input = sys.stdin.readline()
n, m = map(int, input.split())

# 1부터 n까지의 숫자 중 m개를 뽑는 순열 생성 (중복허용 x)
for seq in permutations(range(1, n + 1), m):
    print(' '.join(map(str, seq)))