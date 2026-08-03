T = int(input())
rst = []

for test_case in range(0,T):
    card_num = int(input())
    card_lst = input().split()
    
    rst_str = ''
    
    if len(card_lst) % 2 == 0:
        mid = int(card_num/2)
        half1 = [card_lst[x] for x in range(0, mid)]
        half2 = [card_lst[x] for x in range(mid, card_num)]
        
        for i in range(0, mid):
            if i != mid-1:
                rst_str += half1[i] + ' ' + half2[i] + ' '
            else:
                rst_str += half1[i] + ' ' + half2[i]
                       
    else:
        mid = int(card_num+1/2)
        half1 = [card_lst[x] for x in range(0, mid)]
        half2 = [card_lst[x] for x in range(mid, card_num)]
        # half1 is longer than half2
        
        for i in range(0, mid-1):
            rst_str += half1[i] + ' ' + half2[i] + ' '
                
        rst_str += half1[-1]
    
    rst.append([test_case+1, rst_str])
            
for test_case in range(0, T):
    print(f"#{rst[test_case][0]} {rst[test_case][1]}")
        