//Ö÷ÒªÔªËØ
a = [2,2,1,1,1,2,2]
b = list(set(a))
c = []
counta = 0
countb = 0
max = 0
for i in b:
    c.append(a.count(i))       
c.sort()
c.reverse()
if c[0] == c[1]:
    print(-1)
else:
    print(c[0])