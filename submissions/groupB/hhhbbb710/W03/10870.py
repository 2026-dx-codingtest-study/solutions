num = int(input())

def Fibonacci(num):
  if num == 0 : return 0
  elif num == 1 : return 1
  else:
    return Fibonacci(num-1) + Fibonacci(num-2)

print(Fibonacci(num))