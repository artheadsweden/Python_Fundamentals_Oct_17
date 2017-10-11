
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        raise TypeError("Second argument needs to be of type <class> Point")

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


    def __str__(self):
        return f"Point has x value {self.x} and y value {self.y}"

    def tryit(self):
        print(self.x)

def main():
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    p3 = p1 + p2

    print(str(p3))

if __name__ == '__main__':
    main()