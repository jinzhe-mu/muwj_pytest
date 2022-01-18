# 创建一个类
class Person:
    # 在类里创建共有属性
    name = "default"
    age = 0
    gender = 'male'
    weight = 0

    # 在类里创建方法，并调用共有属性进行赋值
    # 多个单个变量定义与引用，单变量过多，定义过于麻烦，在02中改进
    def set_param(self, name, age, gener, weight):
        # 实例变量
        self.name = name
        self.age = age
        self.gender = gener
        self.weight = weight

    def eat(self):
        print(f"{self.name} 在 eating")
        return "他说已经吃饱了"

    def play(self):
        print(f"{self.name}目前年龄{self.age}, 在 playing")
        return "觉得已经玩爽了"

    def jump(self):
        print(f"{self.name} 有{self.weight}的体重，在 jump")
        return f"{self.name}跳的筋疲力尽"


# 实例引用
zs = Person()
zs.set_param("张三", "28", "male", "53kg")
print(zs.eat())
print(zs.play())
print(zs.jump())
print(f"zs的姓名是{zs.name},年龄是{zs.age},他的体重是{zs.weight},性别是{zs.gender}")

