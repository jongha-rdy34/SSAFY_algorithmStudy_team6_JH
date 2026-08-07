T = int(input())
rst = []
for test_case in range(0,T):
    ball = 0
    grass_field = [x for x in input()]
    grass_field_dataset = grass_field
    
    
    data = ''
    for i in range (0, len(grass_field_dataset)):
        # 이전 빠진 놈이 )인 건 아래에서 새는 중
        if grass_field_dataset[i] == '(':
            # print(i, data, ball)
            if data != ')':
                ball += 1
                
                

        data = grass_field.pop()

        # 뺀게 )면, 바로 다음꺼 ball로 가정
        if data == ')':
            ball += 1
            
            # print(data, ball)
            
    rst.append([test_case+1, ball])
    
for t in range(0,T):
    print(f'#{rst[t][0]} {rst[t][1]}')