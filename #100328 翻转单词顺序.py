inp = 'the sky is blue'
a = inp.split()##去掉所有空格
b = a[::-1]##翻转String内元素的顺序
c = ''##一个空的String
for i in b:
    c = c + i + ' '##添加元素后都加一个空格
c.rstrip()##移除开头和结尾的多余空格
print(c)
