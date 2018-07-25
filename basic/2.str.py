a = "hello world"
print(a)
print("{} first character is {}".format(a, a[0]))

# a[3] = 'b' # error str can't change
len(a)

b = """hello
world"""

c = r"hello\n"

a = "hello "

b = "world"

a += b

",".join(["hello", "world"])

a.split(' ')

"hello {0}".format("world")

"hello {0} {0}".format("world")

"hello {}".format("world")

"hello {name} {site}".format(name="world", site="eggman")

"hello {name} {site} {num:.2f}".format(name="world", site="eggman", num=3.14)

a = "hello"

a[0:3]
a[-3:-1]
