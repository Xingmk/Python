# 水仙花数也被称为超完全数字 不变数 自恋数 自幂数
# 阿姆斯特朗数 它是一个3位数 该数字每个位上的立方之和正好等于它本身    例如: $1^3 + 5^3 + 3^3 = 153$

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

# 通过 整除 和 求摸运算 分别找出了 一个三位数字的 个，十，百

# 以下方面可以 实现将一个正整数反转  eg: 12345 --> 54321


num = int(input('num = '))
reversed_number = 0

while num > 0:
    reversed_number = reversed_number * 10 + num % 10
    num //= 10

print(reversed_number)
