import sys
input = sys.stdin.readline

n = int(input())

col = [False] * n
diag1 = [False] * (2 * n - 1)
diag2 = [False] * (2 * n - 1)

count = 0

def queen(r):
    global count
    if r == n:
        count += 1
        return

    for c in range(n):
        d1 = r + c
        d2 = r - c + n - 1
        if col[c] or diag1[d1] or diag2[d2]:
            continue

        col[c] = diag1[d1] = diag2[d2] = True
        queen(r + 1)
        col[c] = diag1[d1] = diag2[d2] = False

queen(0)
print(count)
