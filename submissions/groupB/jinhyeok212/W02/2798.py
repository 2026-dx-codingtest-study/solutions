# 2798번: 블랙잭 - 브루트포스 완전탐색

import sys

max_num = 0  # M을 넘지 않는 합 중에서 가장 큰 값을 저장할 변수(정답)
input = sys.stdin.readline
N, M = map(int, input().split())
a = list(map(int, input().split()))  # 카드에 적힌 숫자 리스트

for i in range(0, N-2): # 삼중 for문 - i는 0 ~ N-3 까지 (뒤에 최소 2장이 남아야 함)
    for j in range(i+1, N-1): # j는 i+1 ~ N-2 까지 (뒤에 최소 1장이 남아야 함)
        for k in range(j+1, N): # k는 j+1 ~ N-1 까지
            s = a[i] + a[j] + a[k]

            if s > M:  # 합이 M을 넘으면 다음 조합으로 넘어감
                continue  
            else:  # M 이하인 경우에만 현재 max_num과 비교해서 갱신
                max_num = max(max_num, s)
print(max_num)

#combination 함수 사용해서 다시 해보기!