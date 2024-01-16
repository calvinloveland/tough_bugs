class Parent():
    def __init__(self):
        self.name = 'Parent'
        self.__value = 100

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.name = 'Child'
        self.__value = 200

if __name__ == '__main__':
    p = Parent()
    print(p.name)
    c = Child()
    print(c.name)
    print(c.__value)