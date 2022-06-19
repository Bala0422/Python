
def jumpingOnClouds(c):
    flag = 0
    jump = 0
    for i in range(len(c) - 2):
        if flag == 1:
            flag = 0
            continue
        if c[i] == 0 and c[i+1] == 0 and c[i+2] == 0:
            jump += 1
            flag = 1
        elif c[i] == 0 and c[i+1] == 0:
            jump += 1
        elif c[i] == 0 and c[i+1] == 1:
            pass
        elif c[i] == 1:
            jump += 1

    if c[len(c)-3] == 0 and c[len(c)-2] == 0 and c[len(c)-1] == 0:
        jump -= 1
    return jump + 1


n = int(input())
c = list(map(int, input().rstrip().split()))
result = jumpingOnClouds(c)

print(result)