# use function

def fac(num):
    """求阶层"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))

print(fac(m) // fac(n) // fac(m-n))
