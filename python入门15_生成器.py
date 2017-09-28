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
print(fblq(10))
#generator和函数的执行流程不一样。函数时顺序执行，遇到return语句
#或最后一行就返回。而generator，在执行next()的时候执行，遇到yield
#返回，再次执行时从上次执行到的yield语句处继续执行。
print('定义一个generator,依次返回1,3,5')
def odd():
	print('step 1')
	yield(1)
	print('step 2')
	yield(2)
	print('step 3')
	yield(3)
o=odd()
print(o)
print('next(o):',next(o))
print('next(o):',next(o))
print('next(o):',next(o))
#print('next(o):',next(o))   #StopIteration
#odd不是普通函数，是generator,遇到yield中断，下次从中断出执行
for y in odd():
	print(y)
#fblq()定义为generator之后，通过for循环遍历
for x in fblq(10):
	print(x)
fb=fblq(10)
while True:
	try:
		x=next(fb)
		print(x)
	except Exception as e:
		print('generator return value',e.value)
		break
#杨辉三角
def triangles(n):
	for i in range(n):
		if i==0:
			t=[1]
		elif i==1:
			t=[1,1]
		else:
			t=[1]+[t[j-1]+t[j] for j in range(1,len(t))]+[1]
		yield t
for i in triangles(10):
	print(i)
