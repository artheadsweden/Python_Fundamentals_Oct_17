
y = 10

def my_func():
    global y
    print(y)
    y += 1


def outer():
    x = 10
    def inner():
        nonlocal x
        print(x)
        x += 1
        return x
    return inner

def main():
    pass


if __name__ == '__main__':
    main()