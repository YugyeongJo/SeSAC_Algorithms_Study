# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYYlGU56XOkDFARc

# 종이 꽃가루가 들어있는 풍선이 NxM 크기의 격자판에 붙어있는데, 어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다고 한다.

# 다음의 경우 가운데 풍선을 터뜨리면 상하좌우의 풍선이 추가로 1개씩 터지면서 총 5개의 꽃가루가 날리게 된다.

 

# NxM개의 풍선에 들어있는 종이 꽃가루 개수A가 주어지면, 한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력하는 프로그램을 만드시오.

# (3<=N, M<=100)

 

# 입력

# 첫 줄에 테스트케이스 수 T, 다음 줄부터 테스트케이스 별로 첫 줄에 N과 M, 이후 N줄에 걸쳐 M개씩 풍선에 든 종이 꽃가루 개수가 주어진다.

 

# 출력

# #과 테스트케이스 번호, 빈칸에 이어 종이 꽃가루의 최대 개수를 출력한다.

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
    
for tc in range(T):
    R, C = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(R)]

    score = 0

    for r in range(R):
        for c in range(C):
            cur_score = matrix[r][c]
            
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    cur_score += matrix[nr][nc]
            
            if cur_score > score:
                score = cur_score
                
    print(f"#{tc+1} {score}")
