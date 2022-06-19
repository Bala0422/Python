num = int(input())


def is_ap(lis):
    lis.sort()
    d = lis[1] - lis[0]
    for i in range(2, len(lis)):
        if (lis[i] - lis[i - 1] != d):
            return False

    return True


def total_ap(matrix):
    count = 0
    j = 0
    k = 3
    for i in range(3):
        if is_ap(matrix[j:k]):
            count += 1
        j += 3
        k += 3

    if is_ap([matrix[0], matrix[3], matrix[6]]):
        count += 1
    if is_ap([matrix[1], matrix[4], matrix[7]]):
        count += 1
    if is_ap([matrix[2], matrix[5], matrix[8]]):
        count += 1
    if is_ap([matrix[0], matrix[4], matrix[8]]):
        count += 1
    if is_ap([matrix[6], matrix[4], matrix[2]]):
        count += 1

    return count


for nu in range(num):
    matrix = []
    for i in range(3):
        matrix.append(input().split(' '))

    new_arr = []
    for i in matrix:
        for j in i:
            new_arr.append(int(j))
    maxi = 0
    new_arr.insert(4, int(((new_arr[1] + new_arr[7] )/ 2)))
    if maxi < total_ap(new_arr):
        maxi = total_ap(new_arr)
    new_arr[4] = int((new_arr[3] + new_arr[5]) // 2)
    if maxi < total_ap(new_arr):
        maxi = total_ap(new_arr)
    new_arr[4] = int((new_arr[0] + new_arr[8]) // 2)
    if maxi < total_ap(new_arr):
        maxi = total_ap(new_arr)
    new_arr[4] = int((new_arr[2] + new_arr[6]) / 2)
    if maxi < total_ap(new_arr):
        maxi = total_ap(new_arr)

    print(f'Case #{nu+1}: {maxi}')













