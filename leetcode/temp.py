def solution(arr, n):
    temp_arr = [0] * n
    return array_split(arr, temp_arr, 0, n - 1)


def array_split(arr, temp_arr, l, r):
    count = 0
    if l < r:
        mid = (l + r) // 2
        count += array_split(arr, temp_arr, l, mid)
        count += array_split(arr, temp_arr, mid + 1, r)
        count += insertion_count(arr, temp_arr, l, mid, r)
    return count


def insertion_count(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0
    while i <= mid and j <= right:

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for itr in range(left, right + 1):
        arr[itr] = temp_arr[itr]

    return count


