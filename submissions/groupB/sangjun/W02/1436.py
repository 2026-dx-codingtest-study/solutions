n = int(input())

num = 666
count = 0
while True:
    six_count = 0
    for i in str(num):
        if i =='6':
            six_count+=1
            if six_count ==3:
                count+=1
                break
        else:
            six_count=0
    if count ==n:
        print(int(num))
        break
    num+=1 
            



