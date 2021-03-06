import os

def read_file(file):
    f = open(file, "rt")
    try:
        for line in f:
            print(line.strip())
    finally:
        f.close()

# context manager
def read_file2(file):
    with open(file) as f:
        for line in f:
            print(line.strip())

# 定义文件查找路径
filename = os.path.join(os.path.dirname(__file__), "w.txt")

read_file(filename)

read_file2(filename)
