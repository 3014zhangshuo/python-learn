a = (1, 2, "hello")

type(a) # >>> tuple

a = tuple()

a = (1)
a = ('hello')
a = (1,)

(1, 2) + (3, 4)

(1, 2) * 3

for x in (1, 2, 3):
    print(x)

a, b = (1, 2)
a, _ = (1, 3) # 默认约束 只关心 a 的赋值

2 in (2, 3, 4) # >>> True

5 not in (3, 4, 2) # >>> True

books = [("name", "a"), ("name", "b")]

("apply", 19.99)
