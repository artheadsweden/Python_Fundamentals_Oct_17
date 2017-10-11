
def list_try(name, name_list = None):
    if name_list is None:
        name_list = []
    name_list.append(name)
    return name_list

def main():
    my_list = []
    my_list = list_try('Anna', my_list)
    my_list = list_try('Peter', my_list)
    print(my_list)

    my_new_list = list_try('Sara')
    print(my_new_list)

    my_new_new_list = list_try('Bob')
    print(my_new_new_list)



if __name__ == '__main__':
    main()