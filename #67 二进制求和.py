//二进制求和
a = '11'
b = '1'//给定的二进制数字

result = 0

for i in range(len(a)):
    result = result + (2 ** i) * int(a[i])
for j in range(len(b)):
    result = result + (2 ** j) * int(b[j])//将二进制数换算成十进制数
    
print(bin(result).replace('0b',''))//十进制数重新转换为二进制数
