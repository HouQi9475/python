print ('========Ramon学Python=========')
#循环。Python中有两种循环
#for...in循环，依次把list,tuple中的每个元素迭代出来
names=['Ramon','Leo','Mike','Jack']
for name in names:
    print (name)
#for x in .. 循环就是把每个元素代入变量x，然后执行缩进块的语句
#计算1-10的整数之和，可以用sum变量做累加
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print (sum)
#python提供一个range函数，可以生成整数序列
print (range(5))
#再通过list()可以转换为list
print(list(range(8)))
print (len(list(range(8))))
#计算0-100的和
sum=0
for x in list(range(101)):
    sum=sum+x
print (sum)
print('=====================')
#第二种循环是while循环，只要条件满足，就不断循环，不满足时退出循环
#比如：计算100以内的奇数之和
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print (sum)
#在循环内部变量n不断自减，直到变为-1时，不再满足while条件，循环退出。
#利用循环依次对list中的每个名字打印出 hello,xxx!
names=['Ramon','Leo','Mike','Jack']
for name in names:
    print('Hello,%s' % name)
print('====break====')
#在循环中，break语句可以提前退出循环
#输出1-20的数字
n=1
while n<=20:
    print(n)
    n=n+1
#在上面基础上加一个条件，大于10就结束循环
n=1
while n<=20:
    if(n>10):# 当n=11时，条件满足，执行break语句
        break# break语句会结束当前循环
    print(n)
    n=n+1
print('END')
print('====continue====')
#continue结束本次循环，跳到下次循环
n=0
while n<11:
    n=n+1
    if(n%2==0):
        continue
    print (n)
    
