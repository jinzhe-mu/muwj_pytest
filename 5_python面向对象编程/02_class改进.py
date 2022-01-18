"""
name(类变量)与self.name(实例变量)的区别：
1、name属性是类变量；
2、self.变量名  的方式，访问的变量，叫做实例变量，每个实例访问都有自己的属性
3、两个都是可以被修改的
4、类变量是需要类来访问的，实例变量需要实例来访问
"""
"""
类方法和实例方法的区别
1、类是不能够直接访问到方法的，需要在方法上端增加一个装饰器 @classmethod，定义成类方法
实例方法是可以访问到方法，（self）代表实例调用方法时，会将实例变量传入
"""


# 创建一个类
# 通过class关键字，进行定义了一个类
class Person:
    # 在类里创建共有属性
    name = "default"
    age = 0
    gender = 'male'
    weight = 0

    # 在类里创建方法，并调用共有属性进行赋值
    # 多个单个变量定义与引用，单变量过多，定义过于麻烦，用__inti__方法进行改进
    # 实例化的时候，首先执行init,将属性都定义在__init__中
    def __init__(self, name, age, gener, weight):
        self.name = name
        self.age = age
        self.gender = gener
        self.weight = weight

    def eat(self):
        return f"{self.name}他说已经吃饱了"

    def play(self):
        return f"{self.name}觉得已经玩爽了"

    def jump(self):
        return f"{self.name}跳的筋疲力尽"


# 类的实例化，创建了一个实例
zs = Person("张三", "28", "male", "53kg")
print(zs.eat())
print(zs.play())
print(zs.jump())
print(f"zs的姓名是{zs.name},年龄是{zs.age},"
      f"他的体重是{zs.weight},性别是{zs.gender}")

