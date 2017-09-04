# -*- coding: utf-8 -*-
print('========Ramon学Python========')
print('    ====字符串和编码====')
#在Python3中，字符串是以Unicode编码的
#8个bit一个字节byte（11111111）最大255
#Unicode用两个字节表示一个字符(生僻的需要四个字节)
#对于单个字符的编码Python提供了ord()函数获取字符的整数表示
print(ord('A'))
print(ord('侯'))
print(ord('琪'))
#chr()把编码转换成对于的字符
print(chr(20399)+chr(29738))
#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
#如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#Python对bytes类型的数据用带b前缀的单引号或双引号表示。
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
x=b'ABC'
print (x)
x='ABC'.encode ('ascii')
print(x)
x='侯琪'.encode ('utf-8')
print(x)
#纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
#含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。

#在Python中，无法显示为ASCII字符的字节，用\x##显示
#反过来，如果我们从网络或者磁盘上读取了字节流，那么读到的数据就是bytes。
#要把bytes转为str，就要用到decode方法。
x=b'ABC'.decode('ascii')
print(x)
x=b'\xe4\xbe\xaf\xe7\x90\xaa'.decode('utf-8')
print(x)
#要统计str包含多少个字符，可以用len()函数
print('侯琪包含'+str(len('侯琪'))+'个字符')
print('Ramon包含'+str(len('Ramon'))+'个字符')
#len()函数计算的是str字符数，如果换成bytes，len()函数就计算字节数
#utf-8编码把一个英文字母编码成一个字节，把通常的汉字编码成三个字节
x=len(b'ABC')
print(r"b'ABC'包含"+str(len(b'ABC'))+'个字节')
x=len(b'\xe4\xb8\xad\xe6\x96\x87')
print(r"len(b'\xe4\xb8\xad\xe6\x96\x87')包含"+str(len(b'\xe4\xb8\xad\xe6\x96\x87'))+'个字节')
x=len('侯琪'.encode ('utf-8'))
print(x)  #  6
print('====格式化====')
#在Python中，格式化方式和C语言是一致的，用%实现
# %d 整数 %s 字符串 %f 浮点数
x='Hello,%s' % 'world'
print (x)
x='Hello,%s happy birthday %d' % ('Ramon',27)
print(x)
x='%03d-%2d' % (5,4)
print(x)
print('====练习====')
print('小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出\'xx.x%\'，只保留小数点后1位：')
x=(85-72)/72*100
print('小明成绩提升了 %.1f %%' % x)
a=int(input('请输入你去年的成绩:'))
b=int(input('再输入你今年的成绩:'))
if(a>b):
    b=(a-b)/b*100
    print('你今年成绩降低了 %.1f %%'% b)
else:
    a=(b-a)/a*100
    print('你今年成绩提升了 %.1f %%'% a)
