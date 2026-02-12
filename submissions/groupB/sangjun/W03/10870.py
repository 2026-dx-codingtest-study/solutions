n = int(input())
list1 = []
for i in range(n+1):
    if i ==0:
        list1.append(0)
    elif i==1:
        list1.append(1)
    else:
        list1.append(list1[i-1]+list1[i-2])

print(list1[n])
