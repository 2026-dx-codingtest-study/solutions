from itertools import combinations
n,m = map(int,input().split(" "))
list1 = list(range(1,n+1))
c = list(combinations(list1,m))

for i in c:
    print(*i)  