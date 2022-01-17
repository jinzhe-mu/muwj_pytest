class MyError(Exception):
    def __init__(self, value):
        self.value = value
        print(f"这是一个异常：{value}")

    def __str__(self):
        return repr(self.value)


def set_age(num):
    if num <= 0 or num >= 200:
        # 调用自定义异常
        raise MyError(f"值不在正确范围内(0<num<200):{num}")

    else:
        print(f"设置的年龄为：{num}")


set_age(int(input("请输入年龄：")))

