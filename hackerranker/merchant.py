import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if ar[i] == ar[j] and ar[i] != 0 and ar[j] != 0:
                print(ar[i], ar[j])
                count += 1
                ar[i] = 0
                ar[j] = 0

    return count


n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)


print(result)
