nums = [10,36,30,47,60]
target = 40
result = []
for i in nums:
    if (target - i) in nums:
        if i not in result:
            result.append(i)
            result.append(target - i)
print(result)