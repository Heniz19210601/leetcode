inp = [1,2,3,2,2,2,5,4,2]
e = set(inp)##获取所有不重复的元素
r = []##预设一个列表来储存每个元素出现的次数
m = 0##预设index的值
for i in e:
    r.append(inp.count(i))##在r里面添加每个元素出现的次数
for j in r:
    if j == max(r):##在出现次数列表里面获取最高的值
        m = j##最高值所在inp里面的index
n = inp[m]##inp列表里面最高值的值
print(n)
