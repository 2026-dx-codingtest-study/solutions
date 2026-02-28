def divide_paper(row_start, col_start, length):
    global count_minus_one, count_zero, count_one

    first_value = paper[row_start][col_start]
    is_uniform = True
    for r in range(row_start, row_start + length):
        for c in range(col_start, col_start + length):
            if paper[r][c] != first_value:
                is_uniform = False
                break
        if not is_uniform:
            break
    if is_uniform:
        if first_value == -1:
            count_minus_one += 1
        elif first_value == 0:
            count_zero += 1
        else:
            count_one += 1
    else:
        new_length = length // 3

        for i in range(3):
            for j in range(3):
                divide_paper(
                    row_start + i * new_length,
                    col_start + j * new_length,
                    new_length
                )

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

count_minus_one = 0
count_zero = 0
count_one = 0

divide_paper(0, 0, n)

print(count_minus_one)
print(count_zero)
print(count_one)