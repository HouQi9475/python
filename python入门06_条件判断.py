print ('========Ramon学Python=======')
#条件判断
weight=input('输入你的体重(KG):')
height=input('输入你的身高(m):')
weight=float(weight)
height=float(height)
bmi=weight/height/height
print('您的BMI为%.1f'%bmi)
if(bmi<18.5):
    print('体重过轻..')
elif(18.5<=bmi<25):
    print('体重正常..')
elif(25<=bmi<28):
    print('体重过重..')
elif(28<=bmi<32):
    print('肥胖......')
else:
    print('去死吧...')
