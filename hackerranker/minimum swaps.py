def min(arr, start, end):
    mini = 9999
    for i in range(start,  end):
        if arr[i] < mini:
            mini = arr[i]

    return mini


def minimumSwaps(arr):
    swap = 0
    for i in range(len(arr)):
        mini = min(arr, i, len(arr))
        for j in range(i, len(arr)):
            if arr[i] == mini:
                pass
            elif arr[j] == mini:
                temp = arr[i]
                arr[i] = mini
                arr[j] = temp
                swap += 1

    return swap





n = int(input())
arr = list(map(int, input().rstrip().split()))
res = minimumSwaps(arr)

print(res)
