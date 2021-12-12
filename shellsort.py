def insertionsort(nums,gap):
    for i in range(gap,len(nums)):
        target = nums[i]
        j = i
        while j >= gap and target < nums[j-gap]:
            nums[j] = nums[j-gap]
            j -= gap
        nums[j] = target

def shellsort(nums):
    gap = len(nums)//2
    while gap > 0:
        insertionsort(nums, gap)
        gap = gap//2
nums = [1,2,3,4,5,6]
#nums = [10,4,2,8,5,24,84,1,6]
t = nums.copy()
shellsort(nums)
print(nums)
print(sorted(nums))