//移除元素
n = [3,2,2,3]//给出的数组
val = 3//要移除的值
for i in n:
    if i == val:
        n.remove(i)//当数列中出现等于移除值的数字则移除
print(len(n))//返回移除后数组的新长度
