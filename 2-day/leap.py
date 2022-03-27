"""

判断年份 闰年：True  否则：False

"""

year = int(input('please insert year:'))
#  如果代码太长写成一行不方便阅读 可以使用\或着()折行
#  如果年份能够被4整除但同时不能被100整除 或者 能够被400整除
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)
