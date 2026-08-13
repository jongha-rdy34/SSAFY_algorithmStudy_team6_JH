T = int(input())
for t in range(T):
    n = int(input())
    mid = (n-1)//2
    harvest = 0
    
    farm = []
    for i in range(n):
        farm.append([int(x) for x in input()])
    farmT = list(map(list, zip(*farm)))
    
        
    for i in range(n):
        diff = abs(i - mid)
        harv_diff = mid - diff
        harvest += sum(farmT[i][mid-harv_diff:mid+harv_diff+1])
        
    
    print(f'#{t+1} {harvest}')