# 2차원 개념

matrix = [[3, 7, 9], 
          [4, 2, 6], 
          [8, 1, 5]]

# 접근

print(matrix[1][2]) # 6

print("=========")

# 행우선순회
for r in range(3):
    for c in range(3):
        print(matrix[r][c])
        
print("=========")

# 열우선순회
for c in range(3):
    for r in range(3):
        print(matrix[r][c])
        
print("=========")

# 빈 이차원리스트 제작
# 3행 4열짜리 빈 이차원리스트 제작
R = 3
C = 4
matrix = []

for r in range(3):
    row = []
    for c in range(4):
        row.append(0)
    matrix.append(row)
print(matrix)

# matrix[0][0] = 100

# print(matrix)

## 더 편한 방법
matrix = [[0]*4 for _ in range(3)]
### 아래 방법은 불가능(참조가 되기 때문)
# my_lst = [0] * 4

print("=========")

# 입력받기
# matrix = [list(map(int, input().split())) for _ in range(4)]

print("=========")

# 전치
matrix = [[3, 7, 9],
          [4, 2, 6], 
          [8, 1, 5]]

for r in range(len(matrix)):
    for c in range(len(matrix)):
        if not r >= c:
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
print(matrix)

# zip 함수 통한 구현
transposed_matrix = list(map(list, zip(*matrix)))
print(transposed_matrix)