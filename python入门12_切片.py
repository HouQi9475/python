print ('============Ramon学Python=========')
print('====切片====')
#取一个list和tuple的部分元素是常见的操作
arr=['Ramon','Leo','Mike','Jack','John']
print(arr)
#取前三个元素之笨办法
print(arr[0],arr[1],arr[2])
#取前N个元素，也就是取索引为0-(N-1)的元素
def getParam(arr,n):
	m=[]
	for x in range(n):
		m.append(arr[x])
	print(m)
getParam(arr,3)
#对于经常指定索引范围的操作，用循环很繁琐。Python提供了切片操作符slice
#取前三个元素,用一行代码就可以完成切片
print(arr[0:3])
#arr[0:3]表示从索引0开始取，直到索引3，不包括索引3.取0,1,2
#如果第一个元素是0，还可以省略
print(arr[:3])
#也可以从索引1开始，取出两个元素来
print(arr[1:3])
#类似的，既然Python支持arr[-1]取最后一个元素，那么同样支持倒数切片
print(arr[-1])
print(arr[-4:-1])
#先创建一个0-99的数列
L=list(range(100))
print(L)
#通过切片显示前十个
print(L[:10])
#显示后十个数
print(L[-10:])
#前十一到二十个数
print(L[11:21])
#前十个数，每两个取一个
print(L[0:10:2])
#所有数，每五个取一个
print(L[6::5])
# 什么都不写，只写个:就可以复制这个数组
print(L[:])

#tuple也是一种list，只不过它不可变。同样可以进行切片
tup=(1,3,5,7,9,11,13,15,17,19);
print(tup[:3])   #结果还是tuple
#字符串也可以看做是一个list，每个元素是一个字符
strs='HELLOWORLD!'
print(strs[:5])