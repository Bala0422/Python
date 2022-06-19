def counting_sort(arr, exp):
    count_arr = [0] * 10
    out_arr = [0] * len(arr)

    # counting the occurance of all elements in arr
    for i in range(len(arr)):
        count_arr[int((arr[i] / exp)%10)] += 1

    # getting the sorted index of the elements
    for i in range(1, 10):
        count_arr[i] += count_arr[i - 1]

    # putting it to the array and decrementing the values for repetation
    for i in range(len(arr)-1, -1, -1):
        out_arr[count_arr[int((arr[i] / exp)%10)] - 1] = arr[i]
        count_arr[int((arr[i] / exp)%10)] -= 1

    for i in range(0, len(arr)):
        arr[i] = out_arr[i]
    return arr


arr = [170, 45, 75, 90, 802, 24, 2, 66]

max_ele = max(arr)
exp = 1

while max_ele/exp > 0:
    counting_sort(arr, exp)
    exp *= 10
    print(arr)




