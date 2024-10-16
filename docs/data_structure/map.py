# map(function, iterable)
# iterable 덩어리들에 function 적용하기
# But, map 자체의 객체로 되어있음. 입력 형식이 정의되어있지 않음.
# 원하는 형식으로 다시 한번 변환 시켜줘야함.

nums = list(map(int, input().split()))
print(nums)