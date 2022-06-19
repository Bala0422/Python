
from itertools import permutations

nums = list(map(int, input().split()))
out = []
combination = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        value = nums[i] + nums[j]
        if -value in nums[j + 1:] and (nums[i], nums[j], -value) not in combination:
            all_values = permutations([nums[i], nums[j], -value])
            for k in all_values:
                combination.append(k)
            out.append([nums[i], nums[j], -value])

print(out)



