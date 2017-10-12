def func(a):
    return a % 2 == 0

def main():
    numbers = [1, 2, 3, 4]

    result = list(filter(func, numbers))

    result = list(filter(lambda a: a % 2 == 0, numbers))
    print(result)

    result = [n if n % 2 == 0 else n+1 for n in numbers]
    print(result)

if __name__ == '__main__':
    main()