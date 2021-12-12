def bubble(arr):
    for i in range(len(arr)-1):
        change = False
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                change = True
        if not change:
            break


def get_max(arr):
        '''max = 0
        for j in range(len(arr)):
            if arr[max] < arr[j]:
                max = j
        return max'''
        return arr.index(max(arr))

def selection(arr):
    for i in range(len(arr)):
        l = len(arr)-1-i
        idx = get_max(arr[:l+1])
        arr[idx],arr[l] = arr[l],arr[idx]

def cyclic(arr):
    i = 0
    while i < len(arr):
        if arr[i] != i:
            arr[arr[i]],arr[i] = arr[i],arr[arr[i]]
        else:
            i += 1

def insertion(arr):
    for i in range(len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
            else:
                break
def merge(left,right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def mergesort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left,right)

def quick(arr,low,high):
    if low >= high:
        return

    s = low
    e = high
    p = s + (e-s)//2
    m = arr[p]
    while s <= e:
        while arr[s] < m:
            s += 1
        while arr[e] > m:
            e -= 1
        if s <= e:
            arr[s],arr[e] = arr[e],arr[s]
            s += 1
            e -= 1
    quick(arr,low,e)
    quick(arr,s,high)

#arr = [2,10,9,6,3,7,1,3,1,4,23,765,234,8576,314,645,1234,875687,34,0,-1,-6]
#arr= [9,7,8,6,4,5,2,3,1,0]
#arr = [1,2,3,4,5,6,6,0]
arr = [4,1,3,2,5,7,6]
t = arr.copy()
t.sort()
quick(arr,0,len(arr)-1)
print(arr)
print(t)