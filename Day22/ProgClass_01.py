# Program using classes

class Employee:
    def __init__(self,name,address,age,salary):
        self.name=name
        self.age=age
        self.address=address
        self.salary=salary

def show(self):
    print("Name= ",self.name)
    print("age= ",self.age)
    print("address= ",self.address)
    print("salary= ",self.salary)
    da=(self.salary*10)/100
    gs=self.salary+da
    print("Salary= ",gs)

a= input("Enter the name ")
b=int(input("Enter the age "))
c=input("Enter the address ")
d=int(input("Enter the salary "))

e= Employee(a,c,b,d)
e.show()
