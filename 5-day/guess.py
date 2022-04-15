import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('please insert:'))
    if number < answer:
        print('bigger')
    elif number > answer:
        print('smaller')
    else:
        print('you are right')
        break
    print('you have guess %d times' % counter)
    if counter > 7:
        print('you are fool')
