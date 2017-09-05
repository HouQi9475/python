print ('===========Ramon学Python==========')
print ('======dict=======')
#dict全称dictionary，类似于java中的map，使用键值对存储。
d={'Ramon':99,'Leo':88,'Mike':77}
print (d['Leo'])
d['Jack']=59
print (d)
print('判断key是否存在，可以通过in判断,如下:')
print(r"'Ramon' in d :",'Ramon' in d)
print ('二十通过dict提供的get方法，如果Key不存在返回None或自己指定的值')
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
#传入的参数[1,2,3]是一个list，而限时的{1,2,3}说明set内部只有1,2,3三个元素
#重复元素在set中自动被过滤
s=set([1,2,2,3,3,4,4,4])
print (s)
