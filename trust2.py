from collections import deque

T = int(input())

for t in range(T):
    lst = input().split()
    button_num, button_lst = int(lst[0]), deque(x if x.isalpha() else int(x) for x in lst[1:])
    button_dict = {}
    for i in range(0,len(button_lst),2):
        r = button_lst[i]
        b = button_lst[i+1]
        if button_lst[i] not in button_dict:
            button_dict[r] = deque([b])
        else:
            button_dict[r].append(b)
    
    
    llst = [button_lst[2*x+1] for x in range(len(button_lst)//2)]
    max_loc = max(llst)
    max_idx = llst.index(max_loc)
    max_robot = button_lst[max_idx*2]
    
    o_loc = 1
    b_loc = 1
    time = 0
    o_on_btn = False
    b_on_btn = False
    
    for i in range(len(button_lst)//2):
        # 움직일 대상 물색
        moving_robot = button_lst.popleft()
        moving_loc = button_lst.popleft()
        
        # target이 움직이는 동안, 남은 놈 움직일 수 있는 지 확인
        if moving_robot == 'O':
            time_delta = abs(moving_loc - o_loc)
            time += time_delta
            o_on_btn = True

            
            # B가 움직여야하는 지 확인
            if 'B' in button_dict.keys():
                if len(button_dict['B']) != 0:
                    b_btn_loc = button_dict['B'][0]
                    
                    # B가 움직이는 시간이 O 이동시간 보다 길 경우
                    if abs(b_btn_loc - b_loc) > time_delta+1:
                        if (b_btn_loc - b_loc) > 0:
                            b_loc += (time_delta+1)
                            
                        else:
                            b_loc -= (time_delta+1)
                            
                    else:
                        b_loc = b_btn_loc
                        b_on_btn = True
                        
            o_loc = moving_loc
                    
        elif moving_robot == 'B':
            time_delta = abs(moving_loc - b_loc)
            time += time_delta
            b_on_btn = True
            
            # O가 움직여야하는 지 확인
            if 'O' in button_dict.keys():
                if len(button_dict['O']) != 0:
                    o_btn_loc = button_dict['O'][0]
                    
                    # O가 움직이는 시간이 B 이동시간 보다 길 경우
                    if abs(o_btn_loc - o_loc) > time_delta+1:
                        if (o_btn_loc - o_loc) > 0:
                            o_loc += (time_delta+1)
                            
                        else:
                            o_loc -= (time_delta+1)
                        
                        
                        
                    else:
                        o_loc = o_btn_loc
                        o_on_btn = True                    
                    
            b_loc = moving_loc
            
        # 버튼 누르기
        if moving_robot == 'O':
            o_on_btn = False
            time += 1
            button_dict['O'].popleft()
            
        elif moving_robot == 'B':
            b_on_btn = False
            time += 1
            button_dict['B'].popleft()
    
    print(f'#{t+1} {time}')
