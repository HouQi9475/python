print('============Ramon学Python==========')
print('生成器')
print('''
    通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前
面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
    所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出
后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
    在Python中，这种一边循环一边计算的机制，称为生成器：generator。
	''')
#要创建一个generator，有很多种方法。
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L=[x*x for x in range(1,11)]
print(L)
R=(x*x for x in range(1,11)) #generator
print(R)
#L是一个list，而R是一个generator
#
for x in R:
	print(x)
#print(next(R))   StopIteration
#斐波拉契数列  1, 1, 2, 3, 5, 8, 13, 21, 34, ...
print('斐波拉契数列 ')
def fblq(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'ok'
fblq(10)
#要把fblq函数变成generator，只需要把print(b)改为yield b就可以了：
def fblq(max):
	n,a,b=0,0,1
	while n<max:
		yield(b)    #这就是定义generator的另一种方法
		a,b=b,a+b
		n=n+1
	return 'ok'
fblq(10)
