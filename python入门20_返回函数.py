print('==========Ramon学python==========')
#高阶函数除了可以把函数作为参数外，还可以把函数作为返回值。
#实现一个可变参数的求和
def getSum(*args):
	gs=0
	for n in args:
		gs=gs+n
	return gs
print(getSum(3,5,7,8))
#但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
#可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
	def get_Sum():
		gs=0
		for n in args:
			gs=gs+n
		return gs
	return get_Sum
#当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f=lazy_sum(1,2,3,4)
print(f())
print(f)
#在这个例子中，我们在函数lazy_sum中又定义了函数sum，
#并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
#当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，#注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用

#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1=lazy_sum(1,2,3,4)
print(f1)

#闭包
#注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
#返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
	arr=[]
	for i in range(1,4):
		def aa():
			return i*i
		arr.append(aa)
	return arr
f2,f3,f4=count()
print(f2())
print(f3())
print(f4())

