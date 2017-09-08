print('======Leo学Python======')
print (r"===='''多行内容'''====")
print ('''
hello
python
how are you
       ''')
print('====布尔值====')
#true  注意大小写
print(True)
#false
print(False)
#比较结果
print(3>2)
print(2>3)
#布尔值可以用and ,or,not运算
print("====布尔值运算====")
print(True and True)
print(True and False)
print(False and False)
print(True or False)
print(not True)
#if else
print("====if...else...====")
age=input('请输入您的年龄:')
if int(age)>18:
    print('老油条..')
else:
    print('小屁孩..')
print('====空值====')
#python中空值是None.None不能被理解为0，因为0有意义。而None是一个特殊的空值
#变量名：大小写英文字母，数字，_，且不能已数字开头
print('====变量====')
a='ABC'
b=a;
a='DEF'
print(b)
#python常量
print('====常量====')
#常量一般用全部大写字母表示
PI=3.1415923535
print('PI=',PI)
#除法 在Python中有两种除法，一种是 /  计算结果是浮点数，即使是两个整数相除
print('9/3=',9/3)
print('10/3=',10/3)
#一种是 // 称为地板除,两个整数的除法仍是整数.结果永远是整数
print('取整,10//3=',10//3)
print('取余,10%3=',10%3)
