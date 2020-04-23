nums = [10,36,30,47,60]
target = 40
result = []##输出值
for i in nums:
    if (target - i) in nums:##如果目标值减去当前数字的值存在nums列表中则这两个相加必等于s
        if i not in result:##保证不重复
            result.append(i)
            result.append(target - i)##在result里面添加两个数字
print(result)
