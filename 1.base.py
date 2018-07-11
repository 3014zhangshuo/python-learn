# simple hello world method
def hi(name):
    print("hello {}".format(name))

hi("world")

# help command
# help()
# help(str)

# import module
import math
print("64 sqrt is {}".format(math.sqrt(64)))
print("pi is {}".format(math.pi))

a = 'a'
print("a is {}".format(type(a)))

b = 3
print("b is {}".format(type(b)))

c = 3.14
print("c is {}".format(type(c)))

array = [1, 2, 3]
print("array type is {}".format(type(array)))

print("empty string is {}".format(bool('')))
print("string has value is {}".format(bool('a')))
print("zero is {}".format(bool(0)))
print("positive number is {}".format(bool(1)))
print("negetive number is {}".format(bool(-1)))
print("0.0 is {}".format(bool(0.0)))
print("1.1 is {}".format(bool(1.1)))
print("None type is {}".format(type(None)))
print("None is {}".format(bool(None)))

print("2 cubic {}".format(2 ** 3))
print("2 divided by 3 float {}".format(2 / 3))
print("13 divided by 4 int {}".format(13 // 4))
print("13 divided by 4 remain {}".format(13 % 4))
print("positive infinity {}".format(float("inf")))
print("negetive infinity {}".format(float("-inf")))
