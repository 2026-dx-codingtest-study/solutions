N=int(input())
list=[]
for i in range(N):
    a,b = map(int,input().split())
    list.append((a,b))
list.sort()
for i in range(N):
    print(list[i][0],list[i][1])