# 순열 Permutation 메서드 이용하기
# Permutations는 내부에서 입력을 튜플로 한 번 저장.

from itertools import permutations
import sys

input = sys.stdin.readline
n, m = map(int, input().split()) # map 함수를 사용하여 입력을 공백 기준으로 나누고 int로 타입 변환

arr = range(1, n+1) # permutations 함수 첫 번째 인자값으로 반복 가능한(iterable) range를 이용하여 1~n까지 시퀀스화

for i in permutations(arr,m): # permutations 함수의 두 번째 인자값은 정수값이 들어가야 하고, for문으로 수열값들 나열
    print(*i) # 언패킹하여 출력