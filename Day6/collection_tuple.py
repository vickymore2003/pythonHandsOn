# Tuple is collection data type which is ordered adn unchangable, Duplicate elements are allowed

mytuple=("mouse","keyboard","monitor","cpu","printer","scanner")
print(mytuple)
print(mytuple[2])
print(mytuple[3:5])
print(mytuple[-2])
print(mytuple[-5:-3])

#update tuple , convert the tuple in list and then add the element and again convert it back to tuple
mylist=list(mytuple)
mylist[2]="USB"
mytuple=tuple(mylist)
print(mytuple)
print(len(mytuple))

mytuple1=("mouse",) #add a "," after the element to create a tuple with single element or it will be considered as string
print(type(mytuple1))

x=("g","d","c")
y=("1","3","2")
z = x+y
print(z)

del mytuple
print(mytuple)