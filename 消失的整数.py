//消失的整数
nums = [9,6,4,2,3,5,7,0,1]
nums.sort()
for i in range(len(nums)):
    if i < nums[i]:
        print(i)
        break