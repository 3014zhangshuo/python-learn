from itertools import chain, count, repeat

for x in [1, 2, 3] + [3, 4, 5]:
    print(x)

for x in chain([1, 2, 3], [3, 4, 5]):
    print(x)

a = chain([1, 2, 3], [3, 4, 5])
print(a)

for x in count(10):
    if x > 20:
        break
    print(x)

for x in repeat([1, 3], 2):
    print(x)

any([1, 0]) # >>> True
all([1, 0]) # >>> False

max([1, 10, 2])
min([1, 10, 2])

sum(x for x in range(10))
