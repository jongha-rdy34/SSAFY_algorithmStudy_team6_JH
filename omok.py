def checkRow(field, n):
    # 검증을 5를 뺀 idx에서 시작
    max_idx = n-5
    flag = False

    for row in range(n):
        cnt = 0

        for col in range(n):
            if col > max_idx and cnt == 0:
                break

            if field[row][col] == 'o':
                cnt += 1
            else:
                cnt = 0

        if cnt >= 5:
            flag = True
            break

    return flag

def checkDiagonal(field, n):
    flag = False
    max_idx = n-5

    for row in range(max_idx+1):
        cnt = 0

        for col in range(n):
            if field[row][col] == 'o':


            if field[row][col] == 'o':
                cnt += 1
            else:
                cnt = 0
                break

        if cnt >= 5:
            flag = True
            break
    return flag


T=int(input())

for t in range(T):
    n = int(input())
    field = []
    rst = False

    for i in range(n):
        field.append(input().split())

    field_T = list(map(list, zip(*field)))

    # check Row
    if checkRow(field, n):
        rst = True

    # check column
    elif checkRow(field_T, n):
        rst = True

    elif checkDiagonal(field, n):
        rst = True

    if rst:
        print(f"#{t+1} YES")
    else:
        print(f"#{t+1} NO")
