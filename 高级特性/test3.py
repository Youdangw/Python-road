# 列表生成式 实例 例题
# 列表生成即List Comprehensions,是Python内置的非常简单却强大的可以用来创建list的生成式。

print(list(range(1,11)))

# 生成【1x2,2x2,3x3,.......,10x10】
L = []
for x in range(1,11):
    L.append(x * x)

print(L)
# ↑代替上面的代码   还可以加上if判断筛选出偶数的平方
print([x * x for x in range(1,11)if x %2 ==0])

pls = '1234567890'
print([a + b + c  for a in pls for b in pls for c in pls])

d = {'x':'A','y':'B','z':'C'}
print([k + '=' + v for k,v in d.items()])

L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])

# 练习
# 如果list中既包含字符串，有包含整数，由于非字符串类型没有lower()方法，所以列表生成式报错
# 使用内奸的isinstance函数可以判断一个变量是不是字符串

L1 = ['Hello', 'World', 18, 'Apple',None]
L2 = [i.lower() for i in L1 if isinstance(i, str)]
print(L2)