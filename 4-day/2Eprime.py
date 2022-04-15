# 素数 -->  只能被1 和 自身 整除的 大于 1 的整数


from math import sqrt

num = int(input('please insert a int:'))
end = int(sqrt(num))
is_prime = True

for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d is prime_number' % num)
else:
    print('%d is not prime_number' % num)
