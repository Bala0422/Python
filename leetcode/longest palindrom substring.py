def expand_around(s, start, end):

    while True:
        if start == -1:
            return s[start+1: end-1]
        val = s[start:end+1]
        if val != val[::-1]:
            return s[start+1: end-1]
        else:
            start -= 1
            end += 1


s = input()

out = ''
maxi = -1
for i in range(len(s)):
    one = expand_around(s, i, i)
    two = expand_around(s, i, i+1)

    if len(one) > maxi:
        maxi = len(one)
        out = one
    if len(two) > maxi:
        maxi = len(two)
        out = two
    print(one, two)

print(out)






