T = int(input())
import copy

for t in range(T):
    n = int(input())
    matrix = []
    core_num = 0
    core_idx_lst = []

    # list 뽑아내면서 core의 갯수와 어디에 위치해 있는 지 뽑아낸다.
    for i in range(n):
        row = list(map(int, input().split()))

        for num in range(n):
            if row[num] == 1:
                core_num += 1
                core_idx = [i, num]
                core_idx_lst.append(core_idx)

        matrix.append(row)

    print(core_num, '\n', core_idx_lst)

    cnt = 0
    for i in range(core_num):
        copyed_matrix = matrix.copy()
        copyed_matrix_t = list(map(list, zip(*copyed_matrix)))

        core_idx = core_idx_lst[i]
        core_row, core_col = core_idx

        if 0 in core_idx or n in core_idx:
            pass

        upper = copyed_matrix_t[core_col][0:core_row]
        lower = copyed_matrix_t[core_col][core_row+1:n]
        right = copyed_matrix[core_row][core_col+1:n]
        left = copyed_matrix[core_row][0:core_col]

        