print('==========Ramon学python======')
print('sorted算法')
#排序是经常用到的，无论是冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字
#可以直接比较，那是str或dict呢？那么比较的过程必须通过函数抽象出来
#python内置的sorted函数可以对list进行排序
arr=[-32,-4,6,4,8,1,9]
print(sorted(arr))
#sorted还是一个高阶函数，可以通过key来实现自定义排序，比如按绝对值大小排序
print(sorted(arr,key=abs))
#key指定的函数将作用于数组的每一个元素上，并根据返回的结果排序
arr=['and','Creazy','Zero','ball']
print(sorted(arr))
#对字符串排序，默认是根据ascii码。‘Z’<‘a’
#排序忽略大小写呢？
print(sorted(arr,key=str.lower))
#进行反向排序，加入参数reverse
print(sorted(arr,key=str.lower,reverse=True))
#假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
def by_name(arr):
	return arr[0]
print(sorted(L,key=by_name,reverse=True))