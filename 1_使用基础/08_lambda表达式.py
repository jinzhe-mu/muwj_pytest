"""
可以用lambda关键字来创建一个小的匿名函数
lambda的主题是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去
"""

func2 = lambda x, y: x * y

print(func2(3, 2))

# 功能等同于一下def使用：


def func3(x, y):
    return x*y


print(func3(3, 2))


