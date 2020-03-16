//消失的数字
nums = [9,6,4,2,3,5,7,0,1]//给出的数列
nums.sort()//把数列从小到大排列
for i in range(len(nums)):
    if i < nums[i]://从0开始的有序数列每个数字应该等于index值，若某数字在数列中不等于当前index则缺失的数字必是该index值
        print(i)
        break
