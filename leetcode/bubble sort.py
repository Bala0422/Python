arr = [5, 4, 3, 2, 1]

while True:
    flag = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            temp = arr[i]
            arr[i] = arr[i-1]
            arr[i-1] = temp
            flag = 1
    if flag == 0:
        break

print(arr)

