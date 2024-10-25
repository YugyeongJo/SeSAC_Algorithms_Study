# 델타 탐색

matrix = [[3, 7, 9], 
          [4, 2, 6], 
          [8, 1, 5]]

r, c = 1, 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

print("기준 : ", matrix[r][c])

nr, nc = r+dr[0], c+dc[0]
print("상 이동 : ", matrix[nr][nc])

nr, nc = r+dr[1], c+dc[1]
print("하 이동 : ", matrix[nr][nc])

nr, nc = r+dr[2], c+dc[2]
print("좌 이동 : ", matrix[nr][nc])

nr, nc = r+dr[3], c+dc[3]
print("우 이동 : ", matrix[nr][nc])

# 만일 기준이 외곽이라서 요소가 없다면?
# 인덱스 에러

r, c = 0, 2

for d in range(4):
    nr, nc = r+dr[d], c+dc[d]
    if 0 <= nr < 3 and 0 <= nc < 3:
        print(matrix[nr][nc])