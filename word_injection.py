# 좌측 > 우측으로 검사
def leftRow(puzzle, n, k):
    rst = 0
    for row in puzzle:
        cnt = 0
        for col in range(0, n):

            if row[col] == 1:
                cnt += 1
            else:
                break
            
                    
        if cnt == k:
            rst += 1
            
    if n == k:
        rst = rst/2
        
    return rst

# 우측 > 좌측
def righttRow(puzzle, n, k):
    rst = 0
    for row in puzzle:
        
        cnt = 0
        for col in range(n-1, -1, -1):
            
            if row[col] == 1:
                cnt += 1
            else:
                break
            
        if cnt == k:
            rst += 1
            
    if n == k:
        rst = rst/2
            
    return rst

def upCol(puzzle, n, k):
    rst = 0
    for col in range(0, n):
        
        cnt = 0
        for row in range(n-1, -1, -1):
            if puzzle[row][col] == 1:
                cnt += 1
            else:
                break
            
        if cnt == k:
            rst += 1
            
            
    if n == k:
        rst = rst/2
                    
    return rst

def downCol(puzzle, n, k):
    rst = 0
    for col in range(0, n):
        
        cnt = 0
        for row in range(0,n):
            if puzzle[row][col] == 1:
                cnt += 1
            else:
                break
            
        if cnt == k:
            rst += 1
            
            
    if n == k:
        rst = rst/2
                    
    return rst




T = int(input())
rst_box = []
for test_case in range(0, T):
    n, k = map(int, input().split())
    puzzle = []
    for i in range(0, n):
        puzzle.append(list(map(int, input().split())))

    
    rst_box.append([test_case+1, leftRow(puzzle, n, k)+righttRow(puzzle,n,k)+upCol(puzzle,n,k)+downCol(puzzle,n,k)])
    
    
for test_case in range(0,T):
    print(f"{rst_box[test_case][0]}: {rst_box[test_case][1]}")
    