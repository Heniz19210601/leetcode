//主要元素
a = [2,2,1,1,1,2,2]//提供的数组

b = list(set(a))//提炼不重复元素
c = []
counta = 0
countb = 0
max = 0
for i in b:
    c.append(a.count(i))//统计每个元素重复次数
c.sort()
c.reverse()

if c[0] == c[1]:
    print(-1)
else:
    print(c[0])//判断重复的元素是否有同样多的最高次数
