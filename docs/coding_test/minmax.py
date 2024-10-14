# [입력]

# 첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )

# 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )

# 다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

num = int(input())

for i in range(num):
    count = int(input())
    lst = map(int, input().split())
    max = []
    min = []
    for x in lst:
        if len(max) == 0:
            max.append(x)
        else:
            if max[0] < x:
                max = [x]
        if len(min) == 0:
            min.append(x)
        else:
            if min[0] > x:
                min = [x]
    assert len(max)==1 and len(min)==1
    answer = max[0]-min[0]
    print(f"#{i} {answer}")

