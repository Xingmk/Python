# 使用两个骰子，玩家通过摇两个骰子获得点数进行游戏。

# 简单规则是: 玩家第一次摇骰子 摇出了 7或者11--> 玩家胜
# 玩家第一次摇骰子 摇出了 2，3或者12 --> 庄家胜

# 其他点数的玩家继续摇骰子， 如果玩家摇出了 7点 -->庄家胜
# 如果玩家摇出了 第一次摇出的点数 --> 玩家胜;
# 其他点，玩家继续要骰子，直到分出胜负。

from random import randint

money = 1000
while money > 0:
    print('your assets:', money)
    needs_go_on = False
    while True:
        debt = int(input('please bet:'))
