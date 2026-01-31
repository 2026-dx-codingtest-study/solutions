N = int(input())

i = 666  
title_list = []  #제목이 될수 있는 숫자를 추가할 리스트

while True :
  if '666' in str(i):  # i를 문자열로 바꾼후 '666'이 있으면 리스트에 추가
    title_list.append(i)
  i += 1
  if len(title_list) >= 10000:  # N이 10000보다 작다고 했으니 리스트 갈이가 10000이상이면 멈춤
    break

print(title_list[N-1])  # 인덱스니까 N-1번째 프린트