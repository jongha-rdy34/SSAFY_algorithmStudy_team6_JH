import sys
sys.stdin = open("input.txt", "r")

T = int(input())

'''
cost는 내 마음대로 정할 수 있다.
n으로 설정하면 십자 모양의 부분이 cost임.
 > 넘어가더라도 cost 자체는 변하지 않는다.
'''
def getCost(service_size):
    global house_cnt

    service_output = service_size * service_size + (service_size-1) * (service_size-1)
    for row in range(mat_size):
        for col in range(mat_size):
            cnt = 0
            for house in house_idx:
                x, y = house
                dist = abs(x-row) + abs(y-col)
                if dist < service_size:
                    cnt += 1

            if service_output <= cnt * income:
                house_cnt = max(house_cnt, cnt)


for t in range(T):
    mat_size, income = map(int, input().split())
    city = []

    # house에는 tuple 형태로 (row, col)이 들어간다.
    house_idx = []
    for i in range(mat_size):
        row = list(map(int, input().split()))
        city.append(row)
        if 1 in row:
            for j in range(mat_size):
                if row[j] == 1:
                    house_idx.append((i,j))

    house_cnt = 0

    for k in range(1, mat_size+2):
        getCost(k)

    print(f'#{t+1} {house_cnt}')