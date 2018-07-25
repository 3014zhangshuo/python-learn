f = open("w.txt", mode="rt", encoding="utf-8")
f.read()
f.close()

f = open("w.txt", mode="rt", encoding="utf-8")
f.readlines()

for line in f:
    print(line.strip())
