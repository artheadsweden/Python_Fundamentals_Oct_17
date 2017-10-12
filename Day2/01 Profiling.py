def my_func():
    for n in range(100000):
        y = n**2


def main():
    my_func()
    x = 2
    for i in range(10000000):
        x *= i


if __name__ == '__main__':
    main()