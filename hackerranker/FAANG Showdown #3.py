'''N = int(input())
M = int(input())

arr = []
for i in range(N):
    temp = []
    for j in range(M):
        temp.append(int(input()))

    arr.append(temp)

i = 0
j = 0
direction = 1
for index in range(N*M):
    print(arr[i][j])

    if direction == -1 and i == 0:
        direction = 1
        j += 1
        i -= 1

    if i == N-1 and direction == 1:
        direction = -1
        j += 1
        i += 1

    if direction == 1:
        i += 1

    if direction == -1:
        i -= 1'''

'''N = int(input())
arr = list(map(int, input().split()))

if N == 1:
    print(arr[0])
else:
    required_index = [1, 2]

    sum = required_index[-1] + required_index[-2]
    out_sum = arr[required_index[-1]-1] + arr[required_index[-2]-1]
    while  sum < N:
        sum = required_index[-1] + required_index[-2]
        required_index.append(sum)
        if sum-1 <= N:
            out_sum += arr[sum-1]

    print(out_sum)'''


'''N = int(input())
prev = '1 1 1'
out = ''
for i in range(2, N+1):
    out = str(i) + ' ' + prev + ' ' + str(i) + ' ' + prev+ ' ' + str(i)
    prev = out

if N == 1:
    print(prev)
else:
    print(out)
'''

'''
def Kadane(arr):
    max_sum = arr[0]
    temp = 0
    for i in arr:
        if temp < 0:
            temp = 0
        temp += i
        max_sum = max(max_sum, temp)
    return max_sum


N = int(input())
arr = list(map(int, input().split()))

print(Kadane(arr))'''


'''from itertools import permutations

inputs = int(input())

for inp in range(inputs):
    N = int(input())
    arr = list(map(int, input().split()))
    out = 0
    combination = []
    for i in range(N):
        for j in range(i, N):
            value = arr[i] + arr[j]
            if -value in arr and (arr[i], arr[j], -value) not in combination:
                all_values = permutations([arr[i], arr[j], -value])
                for k in all_values:
                    combination.append(k)
                out += 1

    print(out)
'''

'''
candles = [4, 4, 1, 3]
print(candles.count(max(candles)))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
for i in A:
    if i in B:
        count += 1
        A[A.index(i)] = 0
        B[B.index(i)] = 0

print(count+1)
'''













