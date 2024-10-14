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
