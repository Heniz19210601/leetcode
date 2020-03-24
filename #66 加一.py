##加一
i = [1,2,9]
l = len(i)
i[l-1] += 1
i.reverse()
print(i)
for n in range(l):
    if i[n] > 9:
        i[n+1] += 1
        i[n] = 0
i.reverse()
print(i)
