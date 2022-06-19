n = int(input().strip())

A = list(map(int, input().rstrip().split()))


def problem(ele, arr):
    count = 0
    for i in arr:
        if i < ele:
            count += 1
    return count


def is_sorted(arr):
    if arr[0] < arr[1] < arr[2]:
        return True
    else:
        return False


def reverse(arr):
    return [arr[2], arr[0], arr[1]]


i = 0
while i < n:
    if problem(A[i], A[i+1:]) > 0:
        if is_sorted(A[i:i+3]):
            i += 1


