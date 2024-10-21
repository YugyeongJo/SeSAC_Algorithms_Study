from itertools import accumulate

nums = [3, 5, 1, 4, 2]

acc = list(accumulate(nums))
print(acc)

# 다른 방법
# nums = []
# for i in range(len(nums)):
#     result = sum(nums[:i])
#     acc.append(result)
# print(acc)

