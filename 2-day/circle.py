"""

输入半径计算圆的周长和面积

"""

import math

radius = float(input('please inseart R: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('C: %.2f' % perimeter)
print('S: %.2f' % area)
