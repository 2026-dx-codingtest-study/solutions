N = int(input())
s_list = []  # 생성자를 집어넣을 빈 리스트 생성

for i in range(N):  # N보다 작은 수 모두 탐색
  st_N = str(i)  # 자리수를 하나씩 분리가능하게 문자열로 변경
  s = 0  
  s += i
  for  j in range(len(st_N)):  
    s += int(st_N[j])  # 각 자리의 숫자를 s에 더함
  if s == N: s_list.append(i)  # 분해합이 같다면 리스트에 추가

if len(s_list) == 0: print(0)
else :print(min(s_list))