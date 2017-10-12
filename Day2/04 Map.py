def func(a):
    return a**2

def main():
    numbers = [1, 2, 3, 4]
    result = list(map(func, numbers))

    result2 = (n**2 for n in numbers)

    print(result)
    print(result2)


if __name__ == '__main__':
    main()