"""1
3 3
1 3
2 4
1 4
"""

inp = int(input())
def split_lis(lis, x):
    out = []
    if int(lis[0]) < x < int(lis[1]):
        out.append([int(lis[0]), x])
        out.append([x, int(lis[1])])

    return out


for i in range(inp):
    N, C = input().split(' ')
    range_list = []
    for j in range(int(N)):
        range_list.append(input().split(' '))

    for c in range(int(C)):
        for ele in range(len(range_list)):
            val = split_lis(range_list[ele], c)
            if len(val)  == 2:
                range_list[ele] = val[0]
                range_list.append(val[1])

    print(f'Case #{i+1}: {len(range_list)}')




