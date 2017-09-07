print('=============Ramon学Python=============')
print('====递归函数====')
#在函数内部可以调用其他函数，若函数在内部调用自身，这个函数就是递归函数
#计算n的阶乘 n!=1*2*3*4....*(n-1)*n
#用函数fact(n)表示: fact(n)=n!=(n-1)!*n=fact(n-1)*n
#所以fact(n)=n*f(n-1) n=1时特殊处理
def fact(n):
	if n==1:
		return 1
	return fact(n-1)*n
print(fact(5))

#运用递归写汉诺塔
def move(n,A,B,C):
	if(n==1):
		print(A,'->',C)
	else:
		move(n-1,A,C,B)
		move(1,A,B,C)
		move(n-1,B,A,C)
move(3,'Q','W','E')