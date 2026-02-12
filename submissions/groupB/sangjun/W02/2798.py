from itertools import combinations # 조합함수를 담고있는 모듈
import sys
n, max = sys.stdin.readline().split()
arr = sys.stdin.readline().split()
hap = 0
hap_list = []
for i in combinations(arr,3):
    for k in i:
        hap +=int(k)
    if hap <= int(max):
        hap_list.append(hap)
    hap =0

hap_list = sorted(hap_list, reverse = True)
print(hap_list[0])
            


        

    
    

