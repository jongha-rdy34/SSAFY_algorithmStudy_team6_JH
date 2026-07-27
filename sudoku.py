def rowveri(sudoku,ans):
    veri = True
    for row in range(0,9):
        sudo_row = sudoku[row]
        sudo_row_sorted = sorted(sudo_row)
        if sudo_row_sorted == ans:
            continue
        else:
            veri = False
            break
    return veri


def colveri(sudoku,ans):
    veri = True
    for col in range(0,9):
        sudo_col = []
        for row in range(0,9):
            if sudoku[row][col] in sudo_col:
                veri = False
                break
            else:
                sudo_col.append(sudoku[row][col])

        sudo_col_sorted = sorted(sudo_col)
        if sudo_col_sorted == ans:
           continue
        else:
            veri = False
            break
    return veri

def boxveri(sudoku,ans):
    veri = True
    for fixed_row in range(0, 9, 3):
        for fixed_col in range(0, 9, 3):
            box = []
            for row in range(3):
                for col in range(3):
                    if sudoku[fixed_row+row][fixed_col+col] in box:
                        veri = False
                        break
                    else:
                        box.append(sudoku[fixed_row+row][fixed_col+col])

            if len(box) == 9:
                box_sorted = sorted(box)
                if box_sorted == ans:
                    continue
                else:
                    veri = False
                    break

    return veri

T = int(input())
ans = [x for x in range(1,10)]
rst = []
for test_case in range(0,T):
    sudoku = []
    for row in range(0,9):
        sudoku.append(list(map(int, input().split())))

    if rowveri(sudoku,ans) and colveri(sudoku,ans) and boxveri(sudoku,ans):
        rst.append([test_case+1, 1])
    else:
        rst.append([test_case+1 , 0])

for test_case in range(0,T):
    print(f"#{rst[test_case][0]} {rst[test_case][1]}")