inp = int(input())

for i in range(inp):
    string = list(input())
    W_counts = 0
    R_counts = 0
    flag = 0
    count = 0
    for i in range(len(string)):
        if string[i] == 'W':
            W_counts += 1
        else:
            R_counts += 1

    if string[0] == 'R':
        string[0] = 'W'
        count += 1
    if string[0] == 'W':
        for i in range(0, len(string)):
            if string[i] == 'R':
                flag = i
                break
    for i in range(flag, len(string)):
        if string[i] == 'W':
            count += 1

    if R_counts < count:
        count = R_counts
    if W_counts < count:
        count = W_counts


    print(count)








