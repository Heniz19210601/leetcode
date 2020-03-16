//珠玑妙算
solution = 'RGBY'//给出的正确值和顺序
guess = 'GGRR'//猜测
exist = 0//存在但是位置不对
correct = 0//位置和值都正确
g = []
for i in range(len(guess)):        
    if guess[i] == solution[i]:
        correct = correct + 1//首先获取位置和值都正确的猜测
        g = guess.strip(guess[i])//取出正确值
for i in range(len(g)):
    if g[i] in solution:
        exist = exist + 1//获取所有值是正确的猜测
exist = exist - correct//删除位置和值都正确的数据
print(correct,exist)
