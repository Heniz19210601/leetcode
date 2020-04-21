shorter = 1
longer = 2
k = 3
l = []##所有随机出的总长度列表
while len(l) < k+1:##所有长度的可能性是k+1种
    length = 0
    for i in range(k):##选取k根木板
        length = length + random.randint(shorter,longer)##从长短里随机选取两个相加即得跳板的总长度
    if length not in l:
        l.append(length)##如果计算出的长度不在列表里则添加变成一个新的可能性
l.sort()##从小到大排列
print(l)
