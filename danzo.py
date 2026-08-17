T = int(input())
import copy

def isDanzo(lst):
    rst = -1
    for i in range(len(lst)):
        target_num = lst[i]

        for j in range(i+1, len(lst)):
            multified = target_num * lst[j]
            if rst >= multified:
                break

            multi_to_lst = [int(num) for num in str(multified)]
            veri = sorted(multi_to_lst)

            if multi_to_lst == veri:
                rst = max(rst, multified)


    return rst


for t in range(T):
    n = int(input())
    lst = list(map(int, input().split()))
    # print(lst)
    lst.sort(reverse=True)

    rst = isDanzo(lst)

    print(f'#{t+1} {rst}')