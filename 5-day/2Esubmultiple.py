# 两个数的最大公约数 是 两个数的 公共因子 中最大的那个数;
# 两个书的最小公倍数 是 能够 同时 被两个数整除 的最小的那个数

x = int(input('x = '))
y = int(input('y = '))

# 如果 x > y 就交换 x & y 的值
if x > y:
    x, y = y, x


# 从两个数中较小的开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d 和 %d 的最大公约数是%d' % (x, y, factor))
        print('%d 和 %d 的最小公倍数是%d' % (x, y, x * y // factor))
        break
