//整数反转
number = -120
if number > 0:
    n = str(number)
    n = n[::-1]
else:
    number = number * -1
    n = str(number)
    n = n[::-1]
    n = int(n)
    n = n*-1
print(n)