##拿硬币
coins = [4,2,1]
n = len(coins)
a = 0
for i in coins:
    if i > 2:
        if i % 2 == 0:
            a += (i/2)
        else:
            a += int(i/2)
            a += 1
    else:
        a += 1
print(int(a))