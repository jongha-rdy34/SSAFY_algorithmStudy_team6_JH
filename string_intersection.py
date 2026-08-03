T=int(input())
rst = []

for test_case in range(0,T):
    setA_leng, setB_leng = map(int, input().split())
    setA = set(input().split())
    setB = set(input().split())
    cnt = 0
    
    if setA_leng >= setB_leng:
        for B in setB:
            if B in setA:
                cnt += 1
                
    else:
        for A in setA:
            if A in setB:
                cnt += 1
                
    rst.append([test_case+1, cnt])
    
for t in range(0,T):
    print(f'#{rst[t][0]} {rst[t][1]}')