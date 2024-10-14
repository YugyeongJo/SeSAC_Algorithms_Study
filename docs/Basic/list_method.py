nums = [3, 5, 1, 4, 2]

# append
nums.append(6)
print(nums)

# pop 
print(nums.pop(3))
print(nums)

# sort
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

# 2d sort
nums_2d = [[0, 1], [5, 0], [2, 2]]
nums_2d.sort(key=lambda x : x[1])
print(nums_2d)

# count
print(nums.count(3))

# index
print(nums.index(5))

# insert
nums.insert(1, 9)
print(nums)

# extend
nums.extend([7, 6, 8])
print(nums)
nums += [7, 6, 8]
print(nums)