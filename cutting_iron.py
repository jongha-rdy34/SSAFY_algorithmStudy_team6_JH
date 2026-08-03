T = int(input())
rst = []

for test_case in range(0, T):
    status = input()
    stack = []
    cnt = 0
    # 첫 case 쳐내기
    last_stack = '('
    
    for i in status:
        if i == '(':
            stack.append(i)
            last_stack = stack[-1]
        
        elif i == ')':
            if last_stack == '(':
                stack.append(i)
                last_stack = stack[-1]
                stack.pop()
                stack.pop()
                cnt += len(stack)
            
            elif last_stack == ')':
                stack.append(i)
                last_stack = stack[-1]
                stack.pop()
                stack.pop()
                cnt += 1
        
    rst.append([test_case+1, cnt])

for test_case in range(0, T):
    print(f"#{rst[test_case][0]} {rst[test_case][1]}")