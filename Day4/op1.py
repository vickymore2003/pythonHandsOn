a=8
b=3

#Arithmatic operators
print("The sum is ",a+b)
print("The differance is ",a-b)
print("The product is ",a*b)
print("The Quotient is ",a/b)
print("The remainder is ",a%b)
print("Exponential is ",a**b)
print("The floor division is ",a//b)

#Assignment operators
x = 7
x+=4 # x=x+4
print(x)
x-=3 #x =x-3
print(x)
x*=2 #x=x*2
print(x)
x/=2 #x=x/4
print(x) 
x//=3 #x=x//3
print(x)

#Compare operator
x= 5 
y=7
print(x==y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)

#logical operator, AND OR NOT
print(x>5 and y<10)
print(x>5 or y<10)
print(x!=y)

x=["mango","apple","orange"]
y=["mango","apple","orange"]
#identiy operator , is and is or
print(x is y)       #object are not same eventhough content is same , so use x= y and check again this time it will be true
print(x is not y)


#membership operator, in and not in
print("mango" in x)
print("mango" not in x)