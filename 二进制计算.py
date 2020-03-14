//二进制计算
a = '11'
b = '1'
result = 0
for i in range(len(a)):
    result = result + (2 ** i) * int(a[i])
print(result)
for j in range(len(b)):
    result = result + (2 ** j) * int(b[j])
print(bin(result).replace('0b',''))