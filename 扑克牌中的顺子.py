s = [1,2,3,4,5,6,7,8,9,10,11,12,13,0,0]
m = random.sample(s,5)
m.sort()
if 0 in m:
    m.remove(0)
x = m[len(m)-1] - m[0]
if x > 5:
    print('False')
else: 
    print('True')
print(m)
