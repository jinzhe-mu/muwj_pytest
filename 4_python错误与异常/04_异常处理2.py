def div2(a2, b2):
    return a2 / b2


f = open("data.txt")
try:  # 当下面出现一个异常，异常异常后面的内容将不会被执行
    print(div2(8, 1))
    list1 = [1, 2, 5]
    print(list1[2])
    f = open("data.txt")
    print(f.readline())

except Exception as e:
    print("异常原因：", e)
    print("这里有一个异常")

else:
    print("没有异常的时候执行")

finally:  # finally   最终都会被执行，无论 有异常还是没有异常的情况
    print("finally")
    f.close()  # 如果对一些文件进行操作，可以将关闭文件放在finally下

