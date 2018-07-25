"""User class test

Instance Method must pass self
"""

"""
public
protected
private
"""

class User:

    def __init__(self, name):
        self.name = name

    def hi(self):
        print("hello ", self.name)

    def hello(self):
        self.hi()

    # 不可直接调用
    def __hello(self):
        pass

user = User('zhangshuo')
user.hi()
user.hello()
