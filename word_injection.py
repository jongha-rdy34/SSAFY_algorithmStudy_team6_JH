# 좌측 > 우측으로 검사
def leftRow(puzzle, n, k):
    rst = 0
    for row in puzzle:
        cnt_lst = []
        cnt = 0
        flag = True
        while flag:
            for col in range(0, n):
                if col != n-1:
                    if row[col] == 1:
                        cnt += 1
                    else:
                        cnt_lst.append(cnt)
                        cnt = 0
                else:
                    flag = False
                    if row[col] == 1:
                        cnt += 1
                        cnt_lst.append(cnt)
                    else:
                        cnt_lst.append(cnt)
                        break
                        
        rst += cnt_lst.count(k)
        
    return rst


def upCol(puzzle, n, k):
    rst = 0
    for col in range(0,n):
        cnt_lst = []
        cnt = 0
        flag = True
        while flag:
            for row in range(0, n):
                if row != n-1:
                    if puzzle[row][col] == 1:
                        cnt += 1
                    else:
                        cnt_lst.append(cnt)
                        cnt = 0
                else:
                    flag = False
                    
                    if puzzle[row][col] == 1:
                        cnt += 1
                        cnt_lst.append(cnt)
                        
                    else:
                        cnt_lst.append(cnt)
                        break
                        
        rst += cnt_lst.count(k)
        
    return rst




T = int(input())
rst_box = []
for test_case in range(0, T):
    n, k = map(int, input().split())
    puzzle = []
    for i in range(0, n):
        puzzle.append(list(map(int, input().split())))

    
    rst_box.append([test_case+1, leftRow(puzzle, n, k)+upCol(puzzle,n,k)])
    
    
for test_case in range(0,T):
    print(f"#{rst_box[test_case][0]} {rst_box[test_case][1]}")
    