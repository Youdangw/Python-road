# 迭代  例题 实例
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代(Iteration)

d = {'a': 1, 'b': 2, 'c':3}
for key in d:
    print(key)
print("--------------------------------------")
# 因为dict的储存不是按照list的方式顺序排序，所以，迭代出的结果顺序很可能不一样
# 默认情况下，dict迭代的是key。如果要迭代value，可以用 for value in d.values() ,如果要同时迭代key和value，可以用for k,v in d.items().

for ch in 'ABC':
    print(ch)
print("--------------------------------------")
# 判断一个对象是否可迭代对象  通过collections模块的Iterable类型判断
from collections import Iterable
print('str是否可迭代:',isinstance('abc', Iterable))
print('list是否可迭代:',isinstance([1,2,3],Iterable))
print('整数是否可迭代:',isinstance(123,Iterable))
print("-------------------------------------")
# 下标循环
for i,value in enumerate(['A', 'B', 'C']):
    print(i,value)

print("-------------------------------------")
for x,y in ((1,2),(2,4),(3,9)):
    print(x,y)

#小结
# 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环