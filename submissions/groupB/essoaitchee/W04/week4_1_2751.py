####################################################################################

# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.
# 출력
# 첫째 줄에 N!을 출력한다.

####################################################################################


import sys 

n_list = [] # 정수 저장 list

input = sys.stdin.readline
n = int(input()) # 입력

for i in range(n): # n만큼 반복
  n_num = int(input()) # 숫자 입력
  n_list.append(n_num) # 리스트에 저장

n_list.sort() # 정렬

for j in n_list: # 출력
  print(j)