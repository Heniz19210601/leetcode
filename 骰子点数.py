##60 骰子点数
##把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。
##输入n，打印出s的所有可能的值出现的概率。
n = 7
t = [1,2,3,4,5,6]
p = 6**n
l = n*len(s)
x = l - (n-1)
m = np.ones(x)

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

print(m/p)