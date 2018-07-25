# dictionary 是无序的，key 为不可变类型
a = {"name": "eggman", "url": "https://eggman.tv", "subject":"web development"}

a["name"]

a = dict()

a = dict([("name", "eggman"), ("url", "https://eggman.tv")])

a = dict(name="eggman", url="https://eggman.tv")

a["time"] = "2018/07/24"

del a["time"]

a.get("time", "")

a.update(rating=5, time=2017)

"url" in a # >>> True

for x in a:
    print(x)
    print(a[x])

a.keys()
a.values()

list(a.keys())

for k, v in a.items():
    print(k, v)
