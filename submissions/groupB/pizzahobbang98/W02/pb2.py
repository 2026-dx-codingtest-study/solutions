# 2231 분해합
# 범위 계산 및 역추적
# 임의의 수 N이 주어졌을 때, 생성자(X + X의 각 자리수 합 = N)를 찾는 것
import sys

# 입력 받기
N = int(sys.stdin.readline())
result = 0

# 1부터 N까지 돌면서 생성자 찾기
for i in range(1, N + 1):
    
    # i 값은 나중에 더해야 하므로, 자릿수 계산용 임시 변수에 복사
    num = i 
    digit_sum = 0 # 자릿수의 합을 저장할 변수
    
   
    while num > 0:
        digit_sum += num % 10  
        num //= 10             
    
    # 분해합 = 원래 수(i) + 자릿수 합
    decomposition_sum = i + digit_sum
    
    # 생성자를 찾았으면 저장하고 종료
    if decomposition_sum == N:
        result = i
        break

print(result)