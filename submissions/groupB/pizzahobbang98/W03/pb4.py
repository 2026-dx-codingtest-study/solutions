import sys
from itertools import combinations

# 입력 받기
input = sys.stdin.readline
n, m = map(int, input().split()) # 입력 받은 숫자들을 공백 기준으로 잘라서 정수로 변환

# 1부터 n까지의 숫자 중 m개를 뽑는 조합 생성 (중복허용 x, 오름차순)
for seq in combinations(range(1, n + 1), m): # seq에는 경우의 수가 튜플 형태로 담김
    print(' '.join(map(str, seq))) # string으로 형 변환 후 문자열로 합치기(숫자 사이에 공백 주기)