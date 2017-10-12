from functools import reduce

def f(a, b):
    return a if a > b else b

def main():
    numbers = [1, 2, 3, 4]
    result = reduce(f, numbers)
    print(result)

if __name__ == '__main__':
    main()