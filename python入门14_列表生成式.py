print('============Ramon学Python===========')
print('====列表生成式====')
#列表生成式是Python非常简单却强大的list生成工具
#要生成[1,2,3,4,5]可以用如下：
print(list(range(1,6)))
#如果要生成[1x1,2x2,3x3,4x4...10x10]呢？方法一是循环
num=[]
for x in range(1,11):
	num.append(x*x)
print(num)
#循环太繁琐，列表生成式可以用一行代码实现
print([x*x for x in range(1,11)])
#把要生成的元素放前面，后面跟for循环
#for循环后还可跟条件。只要偶数平方和
print([x*x for x in range(1,21) if x % 2 == 0])
#还可以使用双层循环，生成全排列
print([m+n for m in 'ABC' for n in 'XYZ'])
#列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
print([d for d in os.listdir('.')])
#列表生成式也可以用两个变量来生成List
arr={'name':'leo','age':'23','city':'tj'}
print([key +'->'+value for key,value in arr.items() ])
#把list中的所有字符串变成小写
arr=['Admin','Root','HELLO','WORLD']
print([x.lower() for x in arr])
#如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
L = ['Hello', 'World', 18, 'Apple', None]
print([x.lower() for x in L if isinstance(x,str)])