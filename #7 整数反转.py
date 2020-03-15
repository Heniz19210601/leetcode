//整数反转
number = -120//给出的数字

if number > 0://当数字为正数时
    n = str(number)//整数改换成string
    n = n[::-1]//可直接倒序排列string
    n = int(n)
else:
    number = number * -1//当数字为负数时改变成正数再在最后添加负号
    n = str(number)
    n = n[::-1]
    n = int(n)
    n = n*-1
print(n)
