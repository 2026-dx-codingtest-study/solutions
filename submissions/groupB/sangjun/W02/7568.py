n = int(input())
p =[]
for i in range(1,n+1):
    j,b =map(int,input().split(" "))
    p.append([j,b])
  
for k in p:
    count = 0
    for j in range(len(p)):
        if k[0]<p[j][0] and k[1]<p[j][1]:
            count+=1
    k.append(count+1)
    
for m in p:
    print(m[2], end =' ')