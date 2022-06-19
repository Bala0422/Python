arr = [9,7,1,2,3,5,4,6,8]
length = len(arr)
for i in range(1, len(arr)):
    key = arr[i]
    temp = None
    for j in range(i-1, -1, -1):
        if key < arr[j]:
            arr[j+1] = arr[j]
            temp = j
        else:
            break
    if temp is not None:
        arr[temp] = key

print(arr)
