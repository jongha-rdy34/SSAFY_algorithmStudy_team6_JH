from collections import deque

T = int(input())

for t in range(T):
    lst = input().split()
    button_num, button_lst = int(lst[0]), lst[1:]
    button_dict = {}
    
    # 시간으로 계산
    for i in range(0, len(button_lst),2):
        if button_lst[i] not in button_dict:
            button_dict[button_lst[i]] = deque([int(button_lst[i+1]) - 1])
            
        else:
            button_dict[button_lst[i]].append(int(button_lst[i+1]) - 1)
            
    time = 0
    
    o_time = 0
    b_time = 0
    
    if 'O' not in button_dict.keys():
        button_dict['O'] = deque([])
    if 'B' not in button_dict.keys():
        button_dict['B'] = deque([])
    
    o = len(button_dict['O'])
    b = len(button_dict['B'])
    o_work = button_dict['O']
    b_work = button_dict['B']
    
    
    
    if o >= b:
        for i in range(o):
            if len(b_work) == 0:
                o_time += o_work.popleft() + 1
            
            else:
                
                if not (o_time == b_time):
                    o_time += o_work.popleft() + 1
                    b_time += b_work.popleft() + 1
                    
                else:
                    if o_work[-1] >= b_work[-1]:
                        o_time += o_work.popleft() + 1
                        b_time += b_work.popleft() + 2
                        
                    else:
                        o_time += o_work.popleft() + 2
                        b_time += b_work.popleft() + 1
                    
                
    else:
        for i in range(b):
            if len(o_work) == 0:
                b_time += b_work.popleft() + 1
            
            else:
                
                if not (o_time == b_time):
                    o_time += o_work.popleft() + 1
                    b_time += b_work.popleft() + 1
                    
                else:
                    if b_work[-1] >= o_work[-1]:
                        o_time += o_work.popleft() + 2
                        b_time += b_work.popleft() + 1
                        
                    else:
                        o_time += o_work.popleft() + 1
                        b_time += b_work.popleft() + 2            
            
    if o_time >= b_time:
        print(f'#{t+1} {o_time}')
    else:
        print(f'#{t+1} {b_time}')