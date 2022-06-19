def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i][0] <= R[j][0]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


intervals = [[1, 4], [0, 2], [3, 5]]
mergeSort(intervals)


out = []
for i in intervals:
    if not out or out[-1][1] < i[0]:
        out.append(i)
    else:
        out[-1][1] = max(out[-1][1], i[1])


print(out)

