def ref_func(x, y):
    return x + y

def main():
    f = (lambda x, y: x + y)(4,5)
    print(f)

    ff = lambda p: lambda b: b**p
    square = ff(2)
    cube = ff(3)

    print(square(3))
    print(cube(3))

if __name__ == '__main__':
    main()