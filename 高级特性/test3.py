# 切片
L = list(range(100))
print(L)

# 前10个数
print(L[:10])

# 后10个数
print(L[-10:])

# 前11-20个数
print(L[10:20])

# 前10个数，每两个取一个
print(L[:10:2])

# 所有数，每五个取一个
print(L[::5])

# 按照原样复制一个list
print(L[:])

# tuple也是一种list  tuple不可变。tuple可切片操作，操作的结果仍是tuple
print((0,1,2,3,4,5)[:3])

# 字符串'xxx'也可当做一个list 每个元素就是一个字符。 可切片操作  操作结果仍是字符串
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])