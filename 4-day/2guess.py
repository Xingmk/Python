# 如果 不知到具体循环次数 推荐使用while

import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('please insert:'))
    if number < answer:
        print('smaller')
    elif number > answer:
        print('bigger')
    else:
        print('you are right')
        break
    print('you have guess %d times' % counter)
    if counter > 7:
        print('you are fool')

# break 只能终止它所在的那个循环
# continue 放弃本次循环后续的代码直接进入下一轮循环
