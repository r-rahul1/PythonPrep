def bubble(nums):
    for i in range(len(nums)):
        swapped = False
        for j in range(1,len(nums)-i):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                swapped = True
        if not swapped:
            break

def find(nums,start:0,end):
    idx = start
    for i in range(start+1,end+1):
        if nums[i] > nums[idx]:
            idx = i
    return idx

def selection(nums):
    end = len(nums)-1
    for i in range(len(nums)):
        idx = find(nums,0,end)
        nums[end],nums[idx] = nums[idx],nums[end]
        end -= 1

def insertion(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,0,-1):
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break

nums = [5,4,2,3,1],[3,1,40,38,2,9,34,8,7,5],[],[-10,30,50,0,-2,-8,21,40,70],[1],[1,2,3,4,5]
for num in nums:
    insertion(num)
    print(num)
