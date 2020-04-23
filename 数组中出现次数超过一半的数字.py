inp = [1,2,3,2,2,2,5,4,2]
e = set(inp)
r = []
m = 0
for i in e:
    r.append(inp.count(i))
for j in r:
    if j == max(r):
        m = j
n = inp[m]
print(n)