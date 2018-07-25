a = range(5)

type(a) # >>> <class 'range'>

list(a) # >>> [0, 1, 2, 3, 4]

list(range(5, 10)) # >>> [5, 6, 7, 8, 9]

list(range(1, 10, 2)) # >>>> [1, 3, 5, 7, 9]

for x in range(10):
    print(x)
