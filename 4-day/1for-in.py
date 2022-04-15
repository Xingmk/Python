# 0 ~ 100 求和

sum = 0
for x in range(101):
    sum += x
print(sum)


#  1~100 偶数求和

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

# 1~100 偶数求和

sum = 0
for x in range(1, 101):
    if x % 2 == 0:
        sum += x
print(sum)

# range(101):  -->  0~100 无法取到101
# range (1, 101): --> 1~100的整数  == 前面是闭区间 后面是 开区间
# range (1, 101, 2): --> 1~100的奇数 == 2 是每次 递增的值
# range (100, 0, -2): --> 100~1的偶数 == -2是每次 递减的值
