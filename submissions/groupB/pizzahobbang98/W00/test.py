n = int(input("텍스트 문자열 갯수를 입력하세요: "))
sum=0
is_valid=True
for i in range(n):
    input_str = input("괄호 문자열을 입력하세요: ")
    
    for j in input_str:
        
        if j == '(':
            sum += 1
        
        elif j == ')':
            sum -= 1

        if sum < 0 :
            is_valid=False
            break


    
    ()()()())()
((()))))))))