# https://www.acmicpc.net/problem/2003

# 문제
# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)이 주어진다. 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어진다. 각각의 A[x]는 30,000을 넘지 않는 자연수이다.

# 출력
# 첫째 줄에 경우의 수를 출력한다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
score = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(i, N):
        if sum(score[i:j+1]) == M:
            ans += 1
print(ans)

# ################
# another

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
score = list(map(int, input().split()))

ans = 0

for i in range(N):
    tmp = 0
    for j in range(i, N):
        tmp += score[j]
        if tmp == M:
            ans += 1
            
        elif tmp > M:
            break
print(ans)

# ################
# solution

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
score = list(map(int, input().split()))

start, end = 0, 0
current_sum = 0
ans = 0

while end < N:
    current_sum += score[end]
    end += 1
    
    while current_sum > M and start < end:
        current_sum -= score[start]
        start += 1
        
    if current_sum == M:
        ans += 1
    
print(ans)

# another code

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
score = list(map(int, input().split()))

s = e = 0
tmp = ans = 0

while True:
    if tmp < M:
        if e == N:
            break
        tmp += score[e]
        e += 1
    elif tmp > M:
        tmp -= score[s]
        s += 1
    else:
        ans += 1
        tmp -= score[s]
        s += 1

print(ans)