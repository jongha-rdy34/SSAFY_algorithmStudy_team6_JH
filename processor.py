T = int(input())

def dfs(core_idx, connected_core, wire_len):
    global max_core, min_wire

    # 종료 조건
    if core_idx == core_num:
        if connected_core > max_core:
            max_core = connected_core
            min_wire = wire_len

        elif connected_core == max_core:
            min_wire = min(min_wire, wire_len)

        return

    row, col = core_idx_lst[core_idx]

    # 선택지 시도
    for d in range(4):
        empty_line = can_connect(row, col, d, n, matrix)

        if empty_line != 0:
        # 상태 반영
            change_matrix(row, col, d, n, matrix, 2)
        # 다음 깊이
            dfs(core_idx + 1, connected_core + 1, wire_len + empty_line)
        # 원상복구
            change_matrix(row, col, d, n, matrix, 0)

    dfs(core_idx+1, connected_core, wire_len)


move_row = [1, -1, 0, 0]
move_col = [0, 0, 1, -1]

def can_connect(row, col, d, n, matrix):
    new_row = row + move_row[d]
    new_col = col + move_col[d]
    empty_line = 0

    while 0 <= new_row < n and 0 <= new_col < n:
        if matrix[new_row][new_col] != 0:
            return 0
        new_row += move_row[d]
        new_col += move_col[d]
        empty_line += 1

    return empty_line


# to_change를 받아 전선을 깔거나 원본으로 되돌려 놓음
def change_matrix(row, col, d, n, matrix, to_change):
    new_row = row + move_row[d]
    new_col = col + move_col[d]
    while 0 <= new_row < n and 0 <= new_col < n:
        matrix[new_row][new_col] = to_change
        new_row += 1
        new_col += 1



for t in range(T):
    n = int(input())
    matrix = []
    core_num = 0
    core_idx_lst = []

    # list 뽑아내면서 core의 갯수와 어디에 위치해 있는 지 뽑아낸다.
    for i in range(n):
        row = list(map(int, input().split()))

        for num in range(n):
            if row[num] == 1 and num != 0 and num != n-1:
                core_num += 1
                core_idx = [i, num]
                core_idx_lst.append(core_idx)

        matrix.append(row)


    min_wire = 0
    max_core = 0

    dfs(0, 0, 0)

    print(f'#{t+1} {min_wire}')