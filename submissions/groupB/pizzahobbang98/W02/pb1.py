# 2798 블랙잭
# 조합 완전 탐색
# N장의 카드 중 3장을 골라 합이 M을 넘지 않으면서 M에 최대한 가까운 수를 만드는 것
import sys
# sys.stdin.readline()
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

result = 0
sum=0
length = len(cards)

# 3장의 카드를 뽑아야 하므로 3중 반복문 사용
# 중복 방지 위해 2번째 카드는 i+1 3번째 카드는 j+1 사용
for i in range(length):
    for j in range(i + 1, length):
        for k in range(j + 1, length):
            sum = cards[i] + cards[j] + cards[k]
            
            # 최댓값 갱신
            if sum <= M:
                result = max(result, sum)

print(result)