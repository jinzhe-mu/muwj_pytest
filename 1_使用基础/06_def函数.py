"""函数代码块以def关键词开头，后接函数名称和圆括号()。
冒号起始
注意缩进
圆括号中定义参数
函数说明——文档字符串
return[表达式]结束函数
选择性地返回一个值给调用方
不带表达式的return或者不写return函数，相当于返回None"""


# 函数的定义
# 位置函数
def func1(a, b, c):
    """
    函数func1的作用（加"""""""后回车会自动带出）
    :param a: 参数a输入后路用来计算
    :return:返回值给调用函数的程序使用
    """
    # 使用tab键天机缩进
    # pycharm快捷键 ctrl+d复制一整行
    d = a + b + c
    print("这是做一个函数")
    return d


# 调用函数并传参
s = func1(2, 3, 4)
print(s)

