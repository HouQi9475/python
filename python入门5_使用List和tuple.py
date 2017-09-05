print ('===========Ramon 学Python===========')
#python内置的一种数据类型是列表:list.list是一种有序的集合，可以随时添加和删除元素。
classmates=['Ramon','leo','Zhangsan']
print (classmates)
#变量classmates就是一个list。用len()函数可以获得list元素的个数
print (len(classmates))
#用索引访问list中的元素，从0开始
print (classmates[0])
#要确保索引不越界，所以最后一个元素的索引是 len(classmates)-1
print(classmates[len(classmates)-1])
#要取得最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print (classmates[-1])
print (classmates[-2])
#list是一个可变的有序表，所以可以往list中追加元素到末尾
classmates.append('root')
print (classmates)
#也可以把元素插入到指定的位置，比如索引为1的位置
classmates.insert (1,'admin')
print (classmates)
#要删除list末尾的元素，用pop()方法
classmates.pop()
print (classmates)
#要删除指定位置的元素，用pop(i）方法，其中i是索引位置
classmates.pop(1)
print(classmates)
#要把某个元素替换成别的元素，可以直接复制给对应的索引位置
classmates[1]='Root'
print(classmates)
#list里面的元素的数据类型也可以不同
L=['apple',123,True]
print (L)
#list数组中也可以包含list对象
s=['python','java',['c','c++'],'php']
print(s)
print(len(s))
print ('===============分隔线================')
#另一种有序列表叫 元组：tuple。与list相似，但一旦初始化就不能修改
classmates=('Ramon','Leo','Mike')
print (classmates)
#现在，classmates这个tuple不能变了，它也没有append(),insert()这样的方法。
#可以使用classmates[1],classmates[-1]，但不能赋值给另外的元素
#当你定义一个tuple时，在定义时元素就必须被确定下来
t=(3,)
print (t)
#python在定义只有一个元素的tuple时必须加逗号，来消除数学中()歧义
print ('========小结========')
print ('''
list和tuple是Python内置的有序集合，一个可变一个不可变。
根据需要来选择使用它们。
''')
