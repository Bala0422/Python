'''
Sooryavanshi
def low_freq(list1):
    low_frequent = list1[0]
    maxi = 9999
    for i in range(len(list1)):
        if list1.count(list1[i]) < maxi:
            low_frequent = list1[i]

    return low_frequent


def get_indexes(l1, value):
    ret = []
    for i in range(len(l1)):
        if l1[i] == value:
            ret.append(i)

    return ret


def is_relatedtoall(vip, unique_list, guest_list, relation_list):
    count = 0
    for i in unique_list:
        indexes = get_indexes(guest_list, i)
        temp = []
        for i in indexes:
            temp.append(relation_list[i])
        if vip in temp:
            count += 1

    if count == len(unique_list):
        return True
    else:
        return False


T = int(input())
N, M = map(int, input().split())
flag = 0

guest = []
relation = []
for i in range(M):
    x, y = map(int, input().split())
    guest.append(x)
    relation.append(y)

low_frequent = low_freq(guest)
vips_index = get_indexes(guest, low_frequent)

vips = []
for i in vips_index:
    vips.append(relation[i])

unique_value = set(guest)

for i in vips:
    if is_relatedtoall(i, unique_value, guest, relation):
        print('alive')
        flag = 1

if flag == 0:
    print('dead')

'''



'''
N, L, C = map(int, input().split())
refuel = list(map(int, input().split()))

step = 0
flag = 0
i = C*L - 1
while True:
    if i >= len(refuel):
        break
    if i != 1:
        if refuel[i] == 1:
            step += 1
            i += C*L
        else:
            i -= 1
    else:
        flag = 1
        break

if flag == 1:
    print(-1)
else:
    print(step)
'''


T, N = map(int, input().split())
weight = list(map(int, input().split()))
time = list(map(int, input().split()))

