word = input()

def palindrome(word):
    if word == word[::-1]:
        return print(True)
    else:
        return print(False)
    
palindrome(word)

# two point algorithm
word = input('단어를 입력하세요: ')

left = 0 # 시작 인덱스
right = len(word)-1 # 마지막 인덱스

is_palindrome = True
while left < right:  # 왼쪽과 오른쪽이 유지될때까지 돌아라!
    if word[left] == word[right]:  # 같은 경우라면 아직은 회문 조건을 만족함
        left += 1  # 왼쪽 포인터를 한칸 오른쪽으로 증가시키고
        right -= 1  # 오른쪽 포인터를 한 칸 왼쪽으로 감소
        continue
    else:  # 다른 경우라면 그 즉시 안된다고 표시하고 break
        is_palindrome = False
        break

print(is_palindrome)