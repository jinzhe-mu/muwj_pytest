import json

# json由字典和列表组成
dict_data = {
    "name": ["jerry", "nicename"],
    "age": 26,
    "gender": "female"
}

print(type(dict_data))
# json.dumps(python_obj)  把数据类型转换成字符串
str_data1 = json.dumps(dict_data)
print(str_data1)
print(type(str_data1))

# json.loads(json_string)     把字符串转换成json
dict_data2 = json.loads(str_data1)
print(dict_data2)
print(type(dict_data2))
