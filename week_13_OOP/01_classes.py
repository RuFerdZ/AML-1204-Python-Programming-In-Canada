import random
import pandas as pd
import names as n


def list_all_employees():
    file_ = pd.read_csv(r"employees.csv")
    employee_name = list(file_["first_name"])
    employee_last = list(file_["last_name"])
    employee_salary = list(file_["salary"])
    employee_dict = {
        "firstnames": employee_name,
        "lastnames": employee_last,
        "salary": employee_salary
    }
    return employee_dict, file_


class Employee:
    # When you call a class, the __init__ method is called by default

    def __init__(self, firstname, lastname, salary):
        print("Employee instance created")
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def register_employee(self):
        file_ = pd.read_csv("employees.csv")
        file_.loc[len(file_)] = [self.firstname, self.lastname, self.salary]
        file_.to_csv("employees.csv", index=False)


salaries = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 120000, 150000, 200000, 250000, 300000]

for x in range(3):
    first_name = n.get_first_name()
    last_name = n.get_last_name()
    instance_john = Employee(firstname=first_name, lastname=last_name, salary=random.choice(salaries))
    # print(instance_john.firstname)
    # print(instance_john)
    instance_john.register_employee()

emp_list, file_ = list_all_employees()
print(emp_list)
print(file_)
