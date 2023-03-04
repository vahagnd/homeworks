nums = [1, 2, 3, 4, 5, 6]
print([sum(nums[:i + 1]) for i in range(len(nums))])