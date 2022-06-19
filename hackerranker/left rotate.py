def rotLeft(a, d):
    out_arr = []
    for i in range(d, len(a)):
        out_arr.append(a[i])
    for i in range(d):
        out_arr.append(a[i])

    return out_arr


nd = input().split()

n = int(nd[0])

d = int(nd[1])

a = list(map(int, input().rstrip().split()))

result = rotLeft(a, d)

print(result)


