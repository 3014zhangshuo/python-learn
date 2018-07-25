# set 可变 无序 不可重复

a = {1, "hello", 2}

type(a) # >>> <class 'set'>

a = {1, "hello", 2, 1}

a = {}

type(a) # >>> <class 'dict'>

a = set()

a.add(1) # >>> {1}

a = set([1, 2, 2, 4]) # >>> {1, 2, 4}

a.remove(4)

a.discard(1)

for x in a:
    print(x)

2 in a # >>> True

a = {1, 3, 5, 2}
b = {1, 4, 7, 3}

a.union(b)

a.intersection(b)

a.difference(b)

{1, 2}.issubset(a) # >>> True

a.issuperset({1, 2}) # >>> True
