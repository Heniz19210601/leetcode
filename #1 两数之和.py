//两数之和
nums = [1,5,2,7,9]//提供的数字
target = 9//目标

first = []
second = []
nums.sort()
result = []

for n in nums:
    if n < (target/2):
        first.append(n)
    else:
        second.append(n)//分解原数列成两个数列
for i in first:
    for j in second:
        if i + j == target:
            result.append(nums.index(i))
            result.append(nums.index(j))//同时搜索两个数列中匹配得和等于目标值的两个数字
print(result)
