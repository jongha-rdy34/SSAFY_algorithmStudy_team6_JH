from collections import deque
T = int(input())

for t in range(T):
    total_num, target_idx = map(int, input().split())

    # 문자열, deque 형태로 받아온다.
    origin = input()
    box = deque([x for x in origin])

    # row가 무조건 4개임으로, 그걸 받아줄 변수를 설정한다.
    row_num = int(total_num/4)

    # 비밀번호가 바뀌어가며 받아놓을 리스트 받아 놓는다.
    changed = []

    # 바뀌는 만큼은 row에 있는 숫자만큼임
    for i in range(row_num):

        # 16진수의 길이 수만큼 때어내가며, 리스트에 따로 저장해놓는다.
        for n in range(0, total_num, row_num):

            # str 슬라이싱 통해서 저장
            changed.append(origin[n:n+row_num])

        # 문자열 바꾸기
        single_chr = box.pop()
        box.appendleft(single_chr)
        origin = single_chr + origin[0:total_num-1]

    # set 통해 겹치는거 지우고, 오름차순으로 정리
    changed = sorted(list(set(changed)), reverse=True)

    # changed에 담긴 것으로 target_index에 해당하는거 16진수로 뽑아내기
    target_num = int(changed[target_idx-1], 16)

    print(f'#{t+1} {target_num}')