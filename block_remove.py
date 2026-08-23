T = int(input())

def dfs(blocks):
    # 1. 종료 조건: 블록이 없으면 0점
    if not blocks:
        return 0

    # 2. 이미 계산해둔 남은 블록 상태라면 저장된 최댓값 바로 반환
    if blocks in memo:
        return memo[blocks]

    max_score = 0
    L = len(blocks)

    # 3. 모든 블록을 하나씩 깨보는 DFS 선택지
    for to_hit in range(L):
        # 점수 계산
        if L == 1:
            hit_score = blocks[0]
        elif to_hit == 0:
            hit_score = blocks[1]
        elif to_hit == L - 1:
            hit_score = blocks[L - 2]
        else:
            hit_score = blocks[to_hit - 1] * blocks[to_hit + 1]

        # 다음 블록 상태
        next_blocks = blocks[:to_hit] + blocks[to_hit + 1:]

        # [이번 점수] + [남은 블록으로 얻을 수 있는 최고 점수 DFS]
        total_score = hit_score + dfs(next_blocks)
        
        # 최댓값 갱신
        if total_score > max_score:
            max_score = total_score

    # 4. 탐색 끝난 결과를 딕셔너리에 기록해둠
    memo[blocks] = max_score
    return max_score


for t in range(1, T + 1):
    hit_max = int(input())
    blocks = tuple(map(int, input().split()))

    memo = {}

    ans = dfs(blocks)
    print(f'#{t} {ans}')