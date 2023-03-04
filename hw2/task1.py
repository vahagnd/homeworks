nums = [0, 1, 2, 3]
k = 15
n = len(nums)
nums = nums[-k % n:] + nums[:-k % n]
print(nums)