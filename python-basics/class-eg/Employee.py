class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,first,last,email,pay):
        self.first = first
        self.last = last
        self.email = email
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



print(Employee.num_of_emps)

emp_1 = Employee('John', 'Doe', 'pavank.d@gmail.com', 50000)
emp_2 = Employee('pavan', 'kumar', 'pavand@sysintell.com', 60000)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

#print(Employee.__dict__)

# print(emp_1)
# print(emp_2)


# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())
# print(emp_2.fullname())

# print(Employee.fullname(emp_1))
# print(Employee.fullname(emp_2))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

print(Employee.num_of_emps)
print(emp_1.num_of_emps)
print(emp_2.num_of_emps)

