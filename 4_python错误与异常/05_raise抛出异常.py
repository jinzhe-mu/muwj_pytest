
def set_age(num):
    if num <= 0 or num >= 200:
        raise ValueError("值不在正确范围内（0<num<200）")

    else:
        print(f"设置的年龄为：{num}")


set_age(int(input("请输入年龄：")))

