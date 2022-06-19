def position(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i


def minimumBribes(q):
    chaot = 0
    for i in range(len(q)):
        i_pos = position(q, i)
        if i_pos == i:
            pass
        else:
            chaot = i_pos - i

        if chaot > 2:
            print('Too chaotic')


t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimumBribes(q)