# 7568 덩치
# 이중 반복 비교
# 나보다 몸무게와 키가 둘 다 큰 사람의 수를 세서 내 등수를 매기는 것

import sys

N = int(sys.stdin.readline())
people = []

# 몸무게랑 키를 리스트에 추가
for _ in range(N):
    # w:weight, h:height
    w, h = map(int, sys.stdin.readline().split())
    people.append((w, h))

# 모든 사람을 한 명씩 기준으로 잡고 전체와 비교
for i in people: # i는 현재 등수를 매길 사람 (본인)
    rank = 1  
    
    for j in people: # j는 비교 대상 (타인)

        # weight와 height가 둘 다 작을 때만 등수 밀려남
        if (i[0] < j[0]) and (i[1] < j[1]):
            rank += 1 
            
    print(rank, end=' ')