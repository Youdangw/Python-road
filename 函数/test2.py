# 递归函数 例题 实例

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(10))

# 垃圾递归 操他妈真鸡巴难
def move(n, a, b, c):
    if(n == 1):
        print(a, "->", c)
        return
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)

move(3,"a","b","c")
