import time
def linearsearch(nums,val):
    for i,num in enumerate(nums):
        if num ==  val:
            return i
    return -1

def binary_search(nums,val):
    left = 0
    right = len(nums)-1
    found = []

    while left <= right:
        mid = (right+left)//2
        if val == nums[mid]:
            found.append(mid)
            left = mid 
        elif val < nums[mid]:
            left = mid+1
        else:
            right = mid-1
    return found


if __name__ == '__main__':
    nums = [1,4,15,15,15,17,21,56]
    f = 15
    print("found the number at",binary_search(nums, f))


    #print("found the number at", linearsearch(nums, f))
