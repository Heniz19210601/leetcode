//两数之和
nums = [1,5,2,7,9]
target = 9
first = []
second = []
nums.sort()
result = []
for n in nums:
    if n < (target/2):
        first.append(n)
    else:
        second.append(n)
for i in first:
    for j in second:
        if i + j == target:
            result.append(nums.index(i))
            result.append(nums.index(j))
print(result)