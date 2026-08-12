from collections import deque
import queue

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
    o_time = 0
    b_time = 0
    o_on_btn = False
    b_on_btn = False
    
    for i in range(len(button_lst)//2):
        robot = button_lst.popleft()
        loc = button_lst.popleft()
        
        if robot == 'O':
            o_time += (loc - o_loc)
            o_on_btn = True
            
            if 'B' in button_dict.keys():
                b_move = button_dict['B'][0]
                
        else:
            b_time += (loc - b_loc)
            b_on_btn = True
            
            
        if (b_time == o_time):
        # 같은 시간에 둘 다 버튼 위에 올라간 경우
            if o_on_btn and b_on_btn: 
                if max_robot == 'O':
                    o_time += 1
                    o_on_btn = False
                    b_time += 1
                    
                else:
                    o_time += 1
                    b_on_btn = False
                    b_time += 1
                
                        
            elif o_on_btn and not b_on_btn:
                
    
    
    
            
    time = 0


    

    if o_time >= b_time:
        print(f'#{t+1} {o_time}')
    else:
        print(f'#{t+1} {b_time}')