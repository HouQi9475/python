print ('=========Ramon学Python=========')
#python的函数定义，除了正常定义必选的参数外，还可以使用默认参数、可变参数和关键字参数
print ('位置参数')
#写一个计算x的平方的函数
def power(a):   #对于函数power(a),参数a就是一个位置参数
	return a*a
#当我们调用该函数时，必须传入且只传入一个参数a
print (power(5))
#那如果要计算x的3,4,5,6...次方呢？
#可以对power函数修改 power(a,n),来计算a的n次方
def power_n(a,n):
	m=1
	while(n>0):
		m=m*a 
		n=n-1
	return m
print (power_n(3,3)) #有两个参数 a,n 这两个参数是位置参数。按位置依次赋值给参数a,n
print('默认参数')
#可以把第二个参数默认为2
def power_n(a,n=2):
	m=1
	while(n>0):
		m=m*a 
		n=n-1
	return m
print('只需输入一个参数a，默认计算平方:',power_n(4))
print(power_n(2,6))
#默认参数可以简化函数的调用，但需要注意：必选参数在前，默认在后
def enrall(name,gender):
	print('name:',name)
	print('gender',gender)
enrall('LEO','M')
#把年龄，城市设置为默认参数，降低调用复杂度
#默认参数必须指向不可变对象
def enrall(name,gender,age=23,city='beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)
enrall('LEO','M')
enrall('Ramon','F',city='tianjin')
#为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内
#部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于
#对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
#我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

print('可变参数')
#可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
#给定a,b,c... 求 a的平方加b的平方加c的平方
#由于参数不确定，可以把参数作为一个List或者tuple传进来
def calc(numbers):
	sum=0
	for num in numbers:
		sum=sum+num*num 
	return sum
print(calc([3,4,5]))
#定义可变参数，在参数前面加一个*号
#在函数内部，参数numbers是一个tuple，因此函数代码完全不变
def calc_new(*numbers):
	sum=0
	for num in numbers:
		sum=sum+num*num 
	return sum
print(calc_new(1,2,3))
#如果已经有个参数List或tuple，使用可变参数过程如下：
a=[1,3,4,5]
print(calc_new(a[0],a[2],a[3]))
#上述写法固然可行，但是太繁琐。可以在数组前加一个*号表示作为可变参数传入
print(calc_new(*a))
#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print('关键字参数')
#可变参数允许传入0个或多个参数，这些参数被自动封装为一个tuple。而关键字参数允许你传入
#0个或任意个含参数名的参数，这些关键字参数在函数内部被自动封装为一个dict
def person(name,age,**kw):
	print('name:',name,'age:',age,'other',kw)
#函数person除了必选参数name和age外，还接收关键字参数kw.调用时可只输入必选参数
person('leo',23)
person('leo',23,hehe='heihei')
print(""" 
关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这
两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，
除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
""")
#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
a={'name1':'leo','age1':23}
person('Ramon',24,ch=a['name1'],ch2=a['age1'])
person('Mike',25,**a)
# **a 是把dict a 所有的key-value 当做关键字参数传入函数的 **kw 参数。
# **kw获得的是dict的拷贝。对**kw的操作并不会影响dict
print('命名关键字参数')
#对于关键字参数，调用者可以传入任意不受限制的关键字参数，可以在函数内部通过kw查看
#通过in可以检查参数是否在关键字参数里  if 'name1' in kw
#如果要限制关键字参数的名字，那么可以使用命名关键字参数，例如只接受City和job的关键字参数
def person_01(name,age,*,city,job):
	print('name:',name,',age:',age,',city:',city,',job:',job)
person_01('jack',23,city='bj',job='coder')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person_02(name, age, *args, city, job):
    print(name, age, args, city, job)
print('参数组合')
#在Python中定义函数，可以用必选参数，默认参数，可变参数，关键字参数，命名关键字参数，自由组合
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'1','2',xiao='haha')
f2(1,2,d=6,email='com')
#通过一个tuple和dict，你也可以调用上述函数：
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args,**kw)
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。