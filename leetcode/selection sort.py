arr = [1, 3, 4,2,9,6,7]

for i in range(len(arr)-1):

    mini = min(arr[i+1:])
    index = arr.index(mini)
    if arr[i] > mini:
        temp = arr[i]
        arr[i] = mini
        arr[index] = temp


print(arr)

