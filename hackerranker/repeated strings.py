
def repeatedString(s, n):
    count = 0
    flag = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count += 1
            flag = 1

    if flag == 1:
        count *= n // len(s)
        rem = n % len(s)
        for i in range(rem):
            if s[i] == 'a':
                count += 1

    return  count


s = input()
n = int(input())
result = repeatedString(s, n)

print(result)

