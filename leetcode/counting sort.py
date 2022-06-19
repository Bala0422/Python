arr = [3, 6, 4, 1, 3, 4, 1, 4]

min_ele = min(arr)
max_ele = max(arr)

rangee = max_ele - min_ele + 1

count_arr = [0] * rangee
out_arr = [0] * len(arr)

# counting the occurance of all elements in arr
for i in range(len(arr)):
    count_arr[arr[i] - min_ele] += 1

# getting the sorted index of the elements
for i in range(1, len(count_arr)):
    count_arr[i] += count_arr[i - 1]

# putting it to the array and decrementing the values for repetation
for i in range(len(arr)):
    out_arr[count_arr[arr[i] - min_ele] - 1] = arr[i]
    count_arr[arr[i] - min_ele] -= 1

print(out_arr)
