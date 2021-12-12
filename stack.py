arr = [i for i in range(1000)]
print(arr)
for i in range(len(arr)):
    if arr[i] == 946:
        print(arr[i])
        break
if 946 in arr:
    print("true")
