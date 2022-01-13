# 通过此方式可以打开一个io的对象
print(open('data.txt'))

f = open('data.txt')
# 查看文件是否是可读的权限
print(f.readable())

# 按行读取
print(f.readline())
print(f.readline())

# 将剩余的文件内容读取出来
print(f.readlines())
# 关闭文件--释放系统内存资源
f.close()
print("-----------------------------------")
# 使用以下操作，就可以不使用.close()操作
# 可以将文件打开后，操作完毕，自动关闭这个文件
# 循环按行读取文件内容
# 图片读取需要使用rb：读取二进制的格式
# 正常的文本，可以使用rt，也就是它的默认格式，可省略
with open('data.txt', 'rt') as e:
    while True:
        line = e.readline()
        if line:
            print(line)
        else:
            break
