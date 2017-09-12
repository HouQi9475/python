print('=============Ramon学python=========')
print('====迭代器====')
#直接作用于for循环的数据类型有：
#一类是集合数据类型，如 list,tuple,dict,set,str
#另一类是generator，包括生成器和带yield的generator function
#这些可以直接作用于for循环的对象统称为可迭代对象 iterable
#可以用isinstance()判断一个对象是否是iterable对象
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('ABC',Iterable))
print(isinstance((x for x in range(3)),Iterable))
print(isinstance(100,Iterable))

#生成器不但可以作用于for循环，还可以被next()函数不断调用并返回
#下一个值，直到最后抛出StopIteration错误表示无法继续返回下个值
#可以被next()函数调用并不断返回下一个值的对象称为迭代器:Iterator
#可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator
print(isinstance((x for x in range(5)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('ABC',Iterator))
#生成器都是Iterator对象，但list,dict,str,tuple虽然是Iterable，
#但不是Iterator。把这些可迭代对象变成迭代器可以使用iter()函数
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter('ABC'),Iterator))
#Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()
#函数调用并不断返回下一个数据，知道没有数据抛出异常。可以把这个数
#据流看作有序序列，但不知道其长度，只能不断next()。惰性的，只有在
#需要返回下一个数据时才会计算
print('小结:')
print("""
	凡是可作用于for循环的对象都是Iterable类型
	凡是可作用于next()函数的对象都是Iterator类型，惰性计算序列
	集合数据类型list,dict,str等是Iterable，而不是Iterator。
	可以通过iter()函数获得Iterator对象
""")