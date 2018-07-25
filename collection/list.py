for x in "hello":
    print(x)

[x for x in "hello"]

[x for x in "hello" if x == 'l']

a = "i love game".split()

[len(x) for x in a]

 {x: len(x) for x in a}

# iterator
b = [1, 3, 4]
x = iter(b)
next(x) # >>> 1
next(x) # >>> 3
next(x) # >>> 4

# Tuple
(x for x in "hello")
z = (x for x in range(1, 1000000000))
next(z)
next(z)
