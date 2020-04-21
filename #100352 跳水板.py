shorter = 1
longer = 2
k = 3
l = []
while len(l) < k+1:
    length = 0
    for i in range(k):
        length = length + random.randint(shorter,longer)
    if length not in l:
        l.append(length)
l.sort()
print(l)