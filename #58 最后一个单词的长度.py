//最后一个单词的长度
s = 'Hello world'//给出的字符串
a = s.split(' ')//把字符串按空格分解
l = len(a)//分解之后有几个单词
if len(a[l-1]) == 0://判定最后一个单词的长度
    print(0)
else:
    print(len(a[l-1]))//输出最后一个单词的长度
