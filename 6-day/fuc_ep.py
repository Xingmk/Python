from random import randint


def rool_dice(n=2):
    """摇色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三个数相加"""
    return a + b + c

# 如果没有指定参数那么使用默认值摇两颗色子


print(rool_dice)
print(rool_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

print(add(c=50, a=100, b=200))
