def my_func(x, y):
    print('Entering my_func')
    if y == 0:
        raise ValueError("Arguemnt y can't be 0")
    z = x / y
    return z



def main():
    try:
        print(my_func(10,0))
    except ValueError as e:
        print(e)
        print(my_func(10,2))
    else:
        print('I did it without errors')
    finally:
        print('Ok lets get out of here')



if __name__ == '__main__':
    main()