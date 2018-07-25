a = [1, 'hello', 'world', True]
a[0] # >>> 1
[1, 2] + [3, 4] # >>> [1, 2, 3, 4]
[1, 2] * 3 # >>> [1, 2, 1, 2, 1, 2]
type(a) # >>> <class 'list'>

b = [1, 2]
b.append(3) # >>> [1, 2, 3] Modify itself

c = list("hello") # >>> ['h', 'e', 'l', 'l', 'o']
len(c) # >>> 5

d = [0, 1, 2, 3, 4]
d[1:3] # >>> [1, 2]
d[:0] = [10, 20] # >>> [10, 20, 0, 1, 2, 3, 4]
d[:] = [] # >>> []

a = [1, 2, 3]
b = [1, 2, 3]
id(a)
id(b)
a is b # False

a = b
a.append(4)

a = b.copy()
a = b[:]

a = [[1,2], [3,4]]

b = a.copy()

a[0].append(3) # => [[1,2,3], [3,4]]
b # => [[1,2,3], [3,4]]

# shadow copy

from copy import deepcopy
a = [[1,2], [3,4]]
b = deepcopy(a)
a[0] is b[0] # => false

a = "my favorite game is the game halo".split()

a.index("game")
a.count("game")

a.remove("game")

del a[0]

'is' in a # >>> True

a.insert(0, 'my')
a.extend([1,2])

a += [3,4] # >>> a = a + [3, 4] 重新开阔一片内存地址

a = [3, 1, 4, 7, 2]
a.sort

a.sort(reverse=True)

sorted(a)
sorted(reverse=True)
