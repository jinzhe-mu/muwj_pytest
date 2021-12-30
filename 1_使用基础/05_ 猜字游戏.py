"""猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字根本给出提示大一点/小一点/猜对了"""
import random

a = random.randint(1, 100)

# print(a)
while True:
    reutle = int(input("请输入0到100的整数："))
    if a == reutle:
        print("恭喜你猜a对了！")
        print("-------------------------------------")
        choice = input("是否继续猜数y/n:")
        if choice == "y":
            a = random.randint(1, 100)
            # print(a)
            continue
        else:
            print("退出游戏！")
            break
    else:
        if a > reutle:
            # print(a, reutle)
            print("你的数字小了一点！请在次猜数！")
            continue
        else:
            # print(a, reutle)
            print("你的数字大了一点！请在次猜数！")
            continue

