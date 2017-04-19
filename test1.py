import math
print(math.sqrt(2))

def power(x, n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

print(power(2,2))

def enroll(name, gender, age = 6, city='Beijing'):
    print("name", name)
    print("gender", gender)
    print("age", age)
    print("city", city)

print(enroll('Sarah', 'F'))

print(enroll('Bob', 'M', '7'))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# *nums 表示把 nums 这个list的所有元素作为可变参数传进去；
nums = [1,2,3]
print(calc(*nums))