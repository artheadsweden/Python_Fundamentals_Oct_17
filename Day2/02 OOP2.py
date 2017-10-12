class Employee:
    raise_amt = 1.04
    def __init__(self, first, last, pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay

    def __str__(self):
        return f"{self.firstname} {self.lastname} earns {self.pay}"

    def give_raise(self):
        self.pay *= self.raise_amt

class Developer(Employee):
    raise_amt = 1.1
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __str__(self):
        return super().__str__() + f' and loves {self.prog_lang}'


def main():
    emp1 = Employee('Anna', 'Jones', 55000)
    emp2 = Employee('John', 'Smith', 47000)

    emp3 = Developer('Sara', 'Andersen', 59000, 'Python')

    if isinstance(emp3,Employee):
        print(emp3.firstname, 'is an employee')
    else:
        print(emp3.firstname, 'is not an employee')

    emp3.give_raise()
    print(emp3)

if __name__ == '__main__':
    main()