##100339 骰子点数

n = 7
t = [1,2,3,4,5,6]##骰子有六个面
z = 6**n##一共有多少种组合
l = n*len(s)
x = l - (n-1)##数学问题 我也无法解释

m = np.ones(x)##创建每个结果的百分比

if n % 2 == 0:
    y = int(x/2)
    for i in range(y):
        m[i+1] = m[i] + 1
    for i in range(y,x-1):
        m[i+1] = m[i] - 1
else: 
    y = round(x/2)
    for i in range(y-1):
        m[i+1] = m[i] + 1
    m[y] = m[y-1]
    for i in range(y,x-1):
        m[i+1] = m[i] - 1
p = m/z
print(p)
