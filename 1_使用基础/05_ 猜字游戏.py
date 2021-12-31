"""猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字根本给出提示大一点/小一点/猜对了"""
import random

computer_number = random.randint(1, 100)

# print(computer_number)
while True:
    person_number = int(input("请输入0到100的整数："))
    if computer_number == person_number:
        print("恭喜你猜a对了！")
        print("-------------------------------------")
        choice = input("是否继续猜数y/n:")
        if choice == "y":
            computer_number = random.randint(1, 100)
            # print(computer_number)
            continue
        else:
            print("退出游戏！")
            break
    else:
        if computer_number > person_number:
            # print(computer_number , person_number)
            print("你的数字小了一点！请在次猜数！")
            continue
        else:
            # print(computer_number , person_number)
            print("你的数字大了一点！请在次猜数！")
            continue

