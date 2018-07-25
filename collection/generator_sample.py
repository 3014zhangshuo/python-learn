from inspect import isgenerator, isgeneratorfunction

def gem_num(ids):
    cached_ids = set()
    for x in ids:
        if x in cached_ids:
            print("cached")
            continue
        yield x
        cached_ids.add(x)

print(isgeneratorfunction(gem_num))
print(isgenerator(gem_num("hello")))

for x in gem_num("hello"):
    print(x)
