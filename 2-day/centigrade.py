"""
华氏温度-->摄氏温度
F = 1.8C +32
"""

f = float(input('please insert Hua:'))
c = (f - 32) / 1.8
print('%.lf Hua = %.lf She' % (f, c))
