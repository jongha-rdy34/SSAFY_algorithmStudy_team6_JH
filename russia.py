T = int(input())

def getMaxBlue(dict):
    blue = []
    for i in range(len(dict)):
        blue.append(dict[i][1])

    max_blue = max(blue)
    return blue.index(max_blue)

for i in range(T):
    flag = []
    flag_dict = {}
    row_num, col_num = list(map(int, input().split()))

    for i in range(row_num):
        row = input()
        flag.append(row)
        flag_dict[i] = [row.count('W'), row.count('B'), row.count('R')]

    max_blue = getMaxBlue(flag_dict)

    cnt = 0

    for i in range(row_num):
        status = 'white'

        # 마지막 줄 흰색 고정
        if i == 0:
            cnt += col_num - flag_dict[i][0]

        # 마지막 줄 붉은색 고정
        if i == row_num-1:
            cnt += col_num - flag_dict[i][2]

        max_color = max(flag_dict[i])
        max_color_idx = flag_dict[i].index(max_color)
        row_dict = flag_dict[i]

        if i <= row_num - 2 and (status == 'white' or status == 'blue'):

            if max_color_idx == 0:
                cnt += col_num - max_color

            else:
                cnt += col_num - row_dict[1]
                status = 'blue'

        