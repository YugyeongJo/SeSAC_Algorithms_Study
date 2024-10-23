# 재귀 스택 오버플로우 방지

def recusion_func():
    
    print("안녕 난 재귀함수야~")
    
    recusion_func()
    
# recusion_func()

# Occur RecursionError

# ====================

import sys
sys.setrecursionlimit(10**9)
# 재귀함수 limit을 재설정하여 에러 방지

def recusion_func(depth):
    if depth == 985:
        return 
    print(f"안녕 난 {depth}번째 재귀함수야~")
    
    recusion_func(depth+1)
    
# recusion_func(0)

# ====================

# 시스템 스택

def find(depth):
    
    if depth == 3:
        print("찾았다!")
        return 
    
    print(f'내려가는 중~ 깊이 : {depth}')
    
    find(depth+1)
    
    print(f'올라가는 중~ 깊이 : {depth}')
    
find(0)

# 재귀함수를 타고 들어가면 재귀함수 호출되는 부분 이후에 작성된 코드는 실행되지 않은 상태로 누적
# 재귀함수가 종료조건을 만나면 종료하는 순서대로 누적되어있는 나머지 실행코드가 실행됨
# So, 위 코드에서 depth가 역으로 출력되는 것을 알 수 있음
# = 시스템 스택