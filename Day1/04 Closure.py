def outer(name):
    def inner(age):
        return f"Hi {name} I see you are {age} years old"
    return inner


def main():
    f = outer('Paul')
    print(f(45))
    f1 = outer('Anna')
    print(f1(34))

if __name__ == '__main__':
    main()