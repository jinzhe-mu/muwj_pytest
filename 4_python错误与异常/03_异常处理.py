# 程序里面要增加处理方式--逻辑过于复杂，一般不推荐
def div(a1, b1):
    if b1 != 0:
        return a1 / b1
    else:
        print("分母 不能为0")
        return 0
print(div(1, 0))


# 多个异常处理方式
def div1(a1, b1):
    return a1 / b1

try:
    print(div1(8, 1))
    list1 = [1, 2, 1]
    print(list1[3])

except ZeroDivisionError as e:
    print("异常原因：", e)
    print("这里有一个异常")
except IndexError as e2:
    print("异常原因：", e2)
    print("这里有一个异常")


# 多个异常推荐捕获方式

def div2(a2, b2):
    return a2 / b2

try:
    print(div2(8, 1))
    list1 = [1, 2, 1]
    print(list1[3])

except Exception as e:
    print("异常原因：", e)
    print("这里有一个异常")

