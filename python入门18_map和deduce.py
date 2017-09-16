print('=========Ramon学python=======')
print('map and reduce')
#python内建了map()和reduce()函数
#map() 接受两个参数。一个是函数，一个是Iterable.map将传入的函数依次作用到序列的每个元素，
#并把结果作为新的Iterator返回。
def f(x):
	return x*x
r=map(f,list(range(10)))
print(list(r))

#map()传入的第一个参数是f,即函数对象本身。由于结果r是Iterator，是惰性序列
#因此通过list()函数计算出整个序列并返回一个list
#map作为高阶函数，事实上它把运算规则抽象了，我们不但可以计算简单的f(x)=x*x
#还可以计算复杂的.比如把 所有数字转为字符串
print(list(map(str,list(range(10))))) #只需一行代码
print('---reduce---')
#reduce把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接受两个参数，
#reduce把结果继续和序列的下一个元素做累积计算，效果是：
print('reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)')
#对一个序列求和
from functools import reduce
def add(x,y):
	return x+y
print(reduce(add,[1,2,3,4,5,6,7,8,9]))
#当然求和可以直接使用内建函数sum()
print(sum([1,2,3,4,5]))
#但如果要把[1,2,5,7,9]变成12579就得用reduce了
def fun(x,y):
	return x*10+y
print(reduce(fun,[1,2,5,7,9]))
#配合map()，把str转换为num
def char2num(x):
	return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}[x]
print(list(map(char2num,'135'))) #[1, 3, 5]
print(reduce(fun,map(char2num,'135')))   #135

#用map()函数将用户输入的不规范单词变为首字母大写
def f2up(x):
	return x[0].upper()+x[1:].lower()
print(list(map(f2up,['LIST','IN','SCHOOL','TEACHER'])))
#编写一个prod函数，接受list并用reduce求和
def prod(arr):
	def ab(a,b):
		return a*b
	return(reduce(ab,arr))
print(prod([1,3,5,7]))