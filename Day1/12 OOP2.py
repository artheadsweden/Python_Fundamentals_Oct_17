class A:
    def __init__(self):
        print('__init__ A')
        self.x = 10

class B(A):
    def __init__(self):
        print('__init__ B')
        super().__init__()
        self.x += 2

class C(A):
    def __init__(self):
        print('__init__ C')
        super().__init__()
        self.x += 4

class D(C, B):
    def __init__(self):
        print('__init__ D')
        super().__init__()

def main():
    d = D()
    print(D.__mro__)


if __name__ == '__main__':
    main()