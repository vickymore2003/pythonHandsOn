#program of factirial using return value
a=int(input("Enter any number : "))

def fact(a):
    f =1
    for x in range(1,a+1):
        f=f*x
    return f

print(fact(a))