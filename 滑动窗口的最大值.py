nums = [1,3,-1,-3,5,3,6,7]
k = 3
n = []
end = len(nums) - k
for i in range(end+1):
    n.append(max(nums[i:i+3]))
print(n)