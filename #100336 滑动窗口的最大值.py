nums = [1,3,-1,-3,5,3,6,7]
k = 3
n = []##预设一个储存最大值的列表
end = len(nums) - k##滑动窗口第一位的位置
for i in range(end+1):##在每一次滑动中
    n.append(max(nums[i:i+k]))##选出窗口内最大值并添加到列表里
print(n)
