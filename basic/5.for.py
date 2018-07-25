a = [1, "hello", "world", 3.14]

for x in a:
    print(x)

for x in a:
    if x == "hello":
        continue
    print(x)

for x in "hello":
    print(x)
