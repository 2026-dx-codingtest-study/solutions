# 단어 정렬

import sys
n = int(sys.stdin.readline())

words = [str(input()) for i in range(n)]

words = list(set(words)) # 단어 중복 제거
words.sort() # 사전 순 정렬
words.sort(key=len) # 길이 순으로 재정렬

for i in words:
    print(i)