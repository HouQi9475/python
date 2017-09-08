print('============Ramon学Python==========')
print('====迭代====')
#如果给定一个list或tuple，我们可以用for循环来遍历。遍历这个过程就叫迭代
#在Python中，迭代是通过 for...in来完成的。
#对dict进行迭代
classmates={'name':'leo','age':23,'city':'TJ'}
for x in classmates:
	print(x)
#因为dict的存储不像list一样顺序存储，所以迭代时可能结果顺序不一致
#默认情况下，迭代的是Key,若要迭代value,如下
for value in classmates.values():
	print(value)
#若要迭代key-value
for key,value in classmates.items():
	print(key,value)
#由于字符串也是可迭代对象，所以可以使用for循环
for x in 'ABCD':
	print(x)
print('判读是否可迭代')
#可以通过collections模块的iterable类别来判断
from collections import Iterable
#str是否可迭代
print(isinstance('ABC',Iterable))
#list是否可迭代
print(isinstance([1,2,3,4],Iterable))
#整数是否可迭代
print(isinstance(688,Iterable))
#python内置的enumerate函数可以把一个list变成索引-值，可以在for中迭代索引和本身
for key,value in enumerate(['A','B','C']):
	print(key,value)
#python中，在for中同时引用两个变量是很常见的
for x,y in ([1,2],[3,4],[5,6]):
	print(x,y)