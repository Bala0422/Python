def extractAreacode(no, d):
    return int(no // pow(10, d - 1)) % 10


def funSort(list, numberofphones, digitpos, maxdigits):
    if digitpos > maxdigits:
        return
    # @start-editable@

    def counting_sort(arr, exp, l):
        count_arr = [0] * 10
        out_arr = [0] * len(arr)

        for i in range(len(arr)):
            count_arr[int((arr[i] / exp) % 10)] += 1

        for i in range(1, 10):
            count_arr[i] += count_arr[i - 1]

        for i in range(len(arr) - 1, -1, -1):
            out_arr[count_arr[int((arr[i] / exp) % 10)] - 1] = l[i]
            count_arr[int((arr[i] / exp) % 10)] -= 1

        for i in range(len(arr)):
            l[i] = out_arr[i]

        return l

    arr = []
    for i in list:
        arr.append(extractAreacode(i, digitpos))

    print(counting_sort(arr, 1, list))

    funSort(list, numberofphones, digitpos + 1, maxdigits)
    # @end-editable@


def getPhoneNumbers():
    phone = []
    noOfElements = int(input())
    while noOfElements > 0:
        element = int(input())
        phone.append(element)
        noOfElements -= 1
    funSort(phone, len(phone), 6, 7)


def main():
    getPhoneNumbers()


if __name__ == '__main__':
    main()

