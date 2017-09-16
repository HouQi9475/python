print('=========Ramon学python=======')
print('filter')
#python内建的filter函数用户过滤序列。和map类似，filter接受一个函数和一个序列
#和map不同的是，filter把传入的函数依次作用于每个元素，然后根据返回值是true还
#是false决定保留还是丢弃该元素
print('在list中，删除偶数，保留奇数')
def is_odd(n):
	return n%2==1
print(list(filter(is_odd,range(10))))
print('把一个序列中的空字符串删掉:')
def del_null(x):
	return x and x.strip()
print(list(filter(del_null,['hello','','world','ramon',None])))
#filter()返回的是一个Iterator，也是个惰性序列，用list()强迫filter完成计算
print('用filter求素数(埃式筛法)')
def _odd_iter():
	n=1
	while True:
		n=n+2
		yield n  #这是一个生成器，并且是一个无限序列
#定义一个函数筛选
def _not_divisible(n):
	return lambda x:x%n>0
#最后，定义一个生成器，不断返回下一个素数
def primes():
	yield 2
	it=_odd_iter() #初始序列
	while True:
		n=next(it) #返回序列的第一个数
		yield n
		it=filter(_not_divisible(n),it) #构建新序列
#这个生成器先返回第一个素数2，然后利用filter不断产生筛选后的新的序列
#由于primes也是一个无限序列，所以调用时需要设置一个退出循环的条件
#打印1000以内的素数
for n in primes():
	if n < 1000:
		print(n)
	else:
		break
#注意到Iterator是惰性计算的序列，所以可用python表示全体素数，自然数这个的序列
