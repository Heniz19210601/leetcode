##拿硬币
coins = [4,2,1]
n = len(coins)
a = 0
for i in coins:
    if i > 2:##如果当前堆的数量大于2个
        if i % 2 == 0:##如果当前堆的硬币可以被2整除
            a += (i/2)##取被2整除的值
        else:
            a += int(i/2)
            a += 1##如果不能被整除，最后增加一次拿取数量为1
    else:
        a += 1##如果小于2个则按1次计算
print(int(a))
