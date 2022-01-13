str_a = 'lili'
str_b = 'babo'
str_age = 28
list1 = [1, 5, 2]
dict1 = {"name": 'tom', "age": 20, "gender": 'male'}
print(f'my name is {str_a},im {str_age} years old, he is {str_b},'
      f'my list is {list1[1]}, my dict si {dict1["gender"]}')

# {}跟表达式（str.uper():转换为大写）
print(f'my name is {str_a.upper()}')

# 如果{}里面要跟‘：’等符号，要加上（）
print(f'result is {(lambda x:x+1)(2)}')

