f = open("w2.txt", "wt")
f.write("hello\n")
f.close

f = open("w2.txt", "at")
f.writelines(["a\n", "b\n"])
f.close
