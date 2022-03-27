"""

英制单位英寸和公制单位厘米互换

"""


value = float(input('please input the length:'))
unit = input('please input the danwei')
if unit == 'in' or unit == 'yingcun'
print('%fyingcun = %fCM' % (value, value * 2.54))
elif unit == 'cm' or unit == 'CM':
print('%CM = %f yingcun' % ( value, value / 2.54))
else:
print('请输入有效的单位')
