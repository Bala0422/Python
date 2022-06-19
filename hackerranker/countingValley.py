def countingValleys(steps, path):
    valley = 0
    level = 0
    for i in range(steps):
        if path[i] == 'U':
            level += 1
        if path[i] == 'D':
            level -= 1
        if level == 0 and path[i] == 'U':
            valley += 1

    return valley


steps = int(input().strip())
path = input()
result = countingValleys(steps, path)
print(result)

