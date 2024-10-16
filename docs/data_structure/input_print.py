# 백준 코딩테스트 풀때, input 받는 방법
import sys
input = sys.stdin.readline

num = input()
print(num.rstrip())
## readline으로 input을 받으면 마지막에 \n이 붙어서 들어옴. so, .rstrip()을 붙여서 사용하여 오류를 보완