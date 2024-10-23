# 피보나치 수열 
def fibo(n):
    if n <= 1 :
        return n
    else:
        return fibo(n-1) + fibo(n-2) 

# n = int(input())
# print(fibo(n))

# 메모이제이션을 통한 풀이(DP의 일종)
N = int(input())
memo = [0, 1]

for _ in range(N-1):
    memo.append(memo[-1] + memo[-2])
    
print(memo[N])

