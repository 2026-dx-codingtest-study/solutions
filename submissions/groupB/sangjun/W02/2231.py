n = int(input())
count = 0 # 생성자가 있는지 없는지를 구분하는 변수
for k in range(1,n+1):
    hap = 0
    for i in str(k):
        hap+=int(i)
    if k+hap == n:
        print(k)
        count+=1
        break
if count ==0:
    print(0)
    


    