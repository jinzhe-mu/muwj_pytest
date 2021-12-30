while True:
    x = float(input("请输入x："))
    if x >= -1:
        if x <= 1 :
            a = x + 2
            print(a)
        else:
            a = 3 * x - 5
            print(a)
    else:
        a = 5*x+3
        print(a)
    a = input("是否继续y/n：")
    if a == "n":
        print("退出计算！")
        break
    else:
        print("继续计算！")


