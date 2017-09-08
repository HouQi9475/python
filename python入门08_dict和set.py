print ('===========Ramon学Python==========')
print ('======dict=======')
#dict全称dictionary，类似于java中的map，使用键值对存储。
d={'Ramon':99,'Leo':88,'Mike':77}
print (d['Leo'])
d['Jack']=59
print (d)
print('判断key是否存在，可以通过in判断,如下:')
print(r"'Ramon' in d :",'Ramon' in d)
print ('二是通过dict提供的get方法，如果Key不存在返回None或自己指定的值')
print(r"d.get('Leo'):",d.get('Leo'))
print(r"d.get('Hello'):",d.get('Hello',-1))

#要删除一个Key,用pop(key)方法，对应的value也会从dict中删除
d.pop ('Jack')
print (d)
#在Python中，dict的key必须是不可变对象。
#dict根据key来计算value的存储位置，通过key计算位置的算法称为哈希算法
#字符串，整数都是不可变的，可以作为key
print ('=====set======')
#set和dict类似，也是一组key的集合，但不存储value。
#由于key不能重复，所以，在set中，没有重复的key
#要创建一个set，需要提供一个list作为输入集合
s=set([1,2,3])
print (s)
#传入的参数[1,2,3]是一个list，而显示的{1,2,3}说明set内部只有1,2,3三个元素
#重复元素在set中自动被过滤
s=set([1,2,2,3,3,4,4,4])
print (s)
#通过add(key)可以将元素添加到set中
s.add(5)
print(s)
#通过remove方法可以删除元素
s.remove(5)
print(s)
#set可以看成数学意义上的无序，无重复的集合，所以这两个可以做交集，并集
a=set([1,3,5,7])
b=set([2,4,5,6])
print(a&b)
print(a|b)
#str是不可变对象，list是可变对象，对可变对象进行操作，内部内容会发生变化
c=[4,3,1,2]
c.sort()
print(c)
c=['c','b','a']
c.sort()
print(c)
#对不可变对象str进行操作
s='abc'
s.replace('a','A')
print(s)
s='abc'
b=s.replace('a','A')
print(b)
print(s)
#当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，
#而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。
#相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，
#就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：