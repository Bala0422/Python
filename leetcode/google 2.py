"""2
5 4
1 2
6 7
9 12
24 24
41 50
14 24 24 4
1 1
42 42
24
"""

inp = int(input())
def mod(num):
    if num < 0:
        return -num
    else:
        return num

def closest(final, q, s):
    min = 99999
    ret = -1
    for i in q:
        temp = mod(int(s) - int(i))
        if temp < min:
            min = temp
            ret = i

    for i in final:
        if int(i) == int(ret):
            q.pop(q.index(ret))
            return closest(final, q, s)

    return ret


for i in range(inp):

    N, M = input().split(" ")
    final = []
    question_paper = []
    for i in range(int(N)):
        question_paper.append(input().split(' '))

    new_arr = []
    for ele in question_paper:
        for j in ele:
            new_arr.append(j)

    student = input().split(' ')

    for i in student:
        final.append(int(closest(final, new_arr, i)))



