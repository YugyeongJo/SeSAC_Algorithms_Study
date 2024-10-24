# https://www.acmicpc.net/problem/8892

# 문제
# 팰린드롬은 어느 방향으로 읽어도 항상 같은 방법으로 읽을 수 있는 단어이다. 예를 들어, civic, radar, rotor, madam은 팰린드롬이다.

# 상근이는 단어 k개 적혀있는 공책을 발견했다. 공책의 단어는 ICPC 문제가 저장되어 있는 서버에 접속할 수 있는 비밀번호에 대한 힌트이다. 비밀번호는 k개의 단어 중에서 두 단어를 합쳐야 되고, 팰린드롬이어야 한다. 예를 들어, 단어가 aaba, ba, ababa, bbaa, baaba일 때, ababa와 ba를 합치면 팰린드롬 abababa를 찾을 수 있다.

# 단어 k개 주어졌을 때, 팰린드롬을 찾는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 공책에 적혀져있는 단어의 수 k(1 ≤ k ≤ 100)가 주어진다. 다음 k개 줄에는 a부터 z까지 알파벳으로 이루어진 단어가 한 줄에 하나씩 주어진다. 모든 단어 길이의 합은 10,000보다 작거나 같다.

# 출력
# 각 테스트 케이스마다 팰린드롬을 출력한다. 만약, 가능한 팰린드롬이 여러 가지라면 아무거나 출력한다. 팰린드롬을 만들 수 없는 경우에는 0을 출력한다.

import sys
input = sys.stdin.readline

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False
    
T = int(input())

def solution(T):
    for _ in range(T):
        N = int(input())
        word = [input().strip() for _ in range(N)]
        
        found_palindrome = False

        for i in range(N):
            for j in range(N):
                if i != j:
                    words = word[i] + word[j]
                    if is_palindrome(words):
                        print(words)
                        found_palindrome = True
                        break
        
            if found_palindrome:
                break

        if not found_palindrome:
            print(0)

solution(T)
                
# =================
from itertools import permutations
T = int(input())

for _ in range(T):
    k = int(input())
    words = [input() for _ in range(k)]
    for w1, w2 in permutations(words, 2):
        p = w1 + w2
        
        if p == p[::-1]:
            print(p)
            break
    
    else:
        print(0)
            