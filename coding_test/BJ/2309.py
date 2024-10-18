# https://www.acmicpc.net/problem/2309

# 문제
# 왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

# 아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

# 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

# 입력
# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

# 출력
# 일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

# ##########################
# solution 1) 이중 for문
dwarfs = [int(input()) for _ in range(9)]
sum_dwarfs = sum(dwarfs)

flag = False
spy = []
for i in range(8):
    for j in range(i+1, 9):
        if sum_dwarfs - dwarfs[i] - dwarfs[j] == 100:
            dwarfs.pop(i)
            dwarfs.pop(j-1)
            # exit(0) # 파일 실행 종료시키는 코드
            flag = True
            break
    if flag:
        break

for dwarf in sorted(dwarfs):
    print(dwarf)

# ##########################
# solution 2) module
# 조합 모듈 활용하기

from itertools import combinations

people = [int(input()) for _ in range(9)]

for this_case in combinations(people, 7):
    if sum(this_case) == 100:
        for person in sorted(this_case):
            print(person)
        break

# ##########################
# solution 3) 재귀

def find_seven_dwarfs(selected, idx):
    # 종료 조건: 7명의 난쟁이를 선택하고 그들의 키의 합이 100인 경우
    if len(selected) == 7 and sum(selected) == 100:
        selected.sort()  # 오름차순 정렬
        list(map(print, selected))  # 결과 출력
        exit()  # 정답을 찾았으므로 프로그램 종료
    # 종료 조건: 7명을 선택했지만 합이 100이 아니거나, 9명을 모두 탐색한 경우
    if len(selected) > 7 or idx >= 9:
        return
    
    # 현재 난쟁이를 선택하는 경우
    find_seven_dwarfs(selected + [people[idx]], idx + 1)
    # 현재 난쟁이를 선택하지 않는 경우
    find_seven_dwarfs(selected, idx + 1)

people = [int(input()) for _ in range(9)]
find_seven_dwarfs([], 0)

# ##########################
# my_code
import sys
input = sys.stdin.readline

people = [int(input()) for _ in range(9)]
sum_num = sum(people)

for i in range(8):
    for j in range(i + 1, 9):
        if sum_num - people[i] - people[j] == 100:
            dwarf1, dwarf2 = people[i], people[j]
            people = [x for x in people if x != dwarf1 and x != dwarf2]
            people.sort()
            break
    else:
        continue
    break

for x in people:
    print(x)