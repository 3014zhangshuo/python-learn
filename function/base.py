def hi():
    print("hi")

hi()

def hi(name):
    print("hi {name}".format(name="zhangshuo"))

hi("zhangshuo")

def hi(name):
    return "hello " + name

hi("zhangshuo")

def hi(a, b=2):
    print(a + b)

hi(10)
hi(10, 20)
hi(b=10, a=30)

# *b tuple **c dict
def hi(a, *b, **c):
    print(a)
    print(b)
    print(c)

hi(1, 2, 3, x=1, y=2)

# passing a method as arguments
def hi(name):
    print(name)

def hello(fuc, name):
    fuc(name)

hello(hi, 'hello')

# nothing execute
def hi():
    pass

hi()

def hi():
    print('a')

a = hi()

print(a) # >>> None

def hi():
    return 1

a = hi()

print(a) # >>> 1

def hi():
    return 1, 2

a = hi()

print(a) # >>> (1, 2)

def hi():
    return 1 if False else 2

a = hi()

print(a) # >>> 2
