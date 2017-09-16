print('===========Ramon学python============')
print('高阶函数')
#Higher-order function
print('---变量可以指向函数---')
#以python内置的求绝对值abs()为例
print(abs(-10))
#如果只写abs呢
print(abs)   #<built-in function abs>
#可见，abs(-10)是函数调用，而abs是函数本身
f=abs
print(f(-2))  #函数本身也可赋值给变量，即变量可以指向函数
#结果表明f已经指向的abs函数本身。
print('---函数名也是变量---')
#函数名就是指向函数的变量。abs是变量，指向求绝对值函数
#一个函数可以接受另一个函数作为参数，这种函数叫做 高阶函数
def add(a,b,fun):
	return fun(a)+fun(b)
print(add(-5,6,abs))
