# 元祖的两中定义方式
tuple_tips1 = (1, 2, 3)
tuple_tips2 = 1, 2, 3
print("tuple_tips1：", type(tuple_tips1), tuple_tips1)
print("tuple_tips2：", type(tuple_tips2), tuple_tips2)


# 列表可变：
list_tips1 = [1, 2, 5, 3]
list_tips1[0] = "a"
print(list_tips1)
# 元祖的不可变特性  运行报错'tuple' object does not support item assignment
# tuple_tips3 = (1, 2, 5, 3)
# tuple_tips3[0] = "a"

# 在元祖里面嵌套列表，列表中的内容是可变的,因为元祖的内存地址没有改变
# 元祖的不可变特性，针对的是变量的指针不可变
list_a = [1, 5, 6]
tuple_tips4 = (5, 8, list_a)
print(id(tuple_tips4))
print(tuple_tips4)
tuple_tips4[2][0] = 'a'
print(id(tuple_tips4))
print(tuple_tips4)



