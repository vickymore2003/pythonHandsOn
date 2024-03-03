
# __init__()
# it is used to initialize the object when the class is crated.
#As when a object is created the __init__() will automaticallt be envoked

class person:
    def __init__(self,name,age):
        self.name = name
        self.age=age
    def show(self):
        print("my name is ",self.name)
        print("my age is ",self.age)
p1=person("Sunny",33)
print("Name= ",p1.name)
print("Age= ",p1.age)

p2=person("vicky",34)
p2.age=35
p2.show()
print(p1)
del(p1)
print(p1)

