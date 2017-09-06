print('=========Ramon学Python=======')
print('====调用函数====')
#Python定义了很多函数，我们可以直接调用
#要调用一个函数，需要知道这个函数的名称和参数
#求绝对值的函数  abs()
a=125
print(abs(a))
b=-34
print(abs(b))
#调用函数时，如果传入的参数类型不正确，会报TypeError错
#TypeError: bad operand type for abs(): 'str'
# c='abc'
# print(abs(c))
print('====max()函数====')
#max()函数可以接受任意个数并返回最大的一个
a=max(1,13,34,23,54,34)
print(a)
# python内置的常用函数还包括数据类型转换，比如Int()
a=int('123')
print(a)
b=int(12.34)
print(b)
#函数名其实就是一个指向函数对象的引用，完全可以把函数名赋值给一个变量 	
#相当于给这个函数起了一个别名
print('====hex()=====')
#利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
a=17
print(hex(a))
a=26
print(hex(a))
a=input('请输入一个整数:')
print('您输入的数的十六进制为:%s' % hex(int(a)))
print('====定义函数====')
#在Python中，定义一个函数需要def语句，依次写出函数名，括号，参数，冒号
#在缩进块中写函数体，返回用return
print('自定义求绝对值函数my_abs()')
def my_abs(m):
	if(m>0):
		return m
	else:
		return -m
print(my_abs(-13.45))
#如果想定义一个什么都不做的空函数，可以用pass
#可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def none():
	pass
#定义新的mynew_abs()函数，增加对参数类型的检查
#数据类型检查可以用内置函数isinstance()实现：
def mynew_abs(x):
	if not isinstance(x, (int,float)):
		raise TypeError('bad operand type')
	if(x>0):
		return x
	else:
		return -x
#print(mynew_abs('a'))
print('====返回多个值====')
#比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标
import math
def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)
#但其实这只是一种假象，Python函数返回的仍然是单一值：
x=move(100,100,60,math.pi/6)
print(x)
print("""
原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
	""")

#定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0 的两个解。
print('求一元二次方程的解')
a=input('请输入方程的第一个参数:')
b=input('请输入方程的第二个参数:')
c=input('请输入方程的第三个参数:')
a=int(a)
b=int(b)
c=int(c)
def quadratic(a,b,c):
	if(a==0):
		return '参数不符合规则'
	elif(b*b<4*a*c):
		return '参数不符合规则'
	else:
		x1=(-b+math.sqrt(b*b-4*a*c))/2*a
		x2=(-b-math.sqrt(b*b-4*a*c))/2*a
		return '该方程的解为 %.3f,%.3f' % (x1,x2)
print(quadratic(a,b,c))