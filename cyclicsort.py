def cyclic(nums):
    i = 0
    while i < (len(nums)):
        if nums[i]-1 != i:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        else:
            i += 1

nums = [5,4,2,3,1],[],[1],[1,2,3,4,5],[2,3,6,7,4,5,1]
for num in nums:
    cyclic(num)
    print(num)