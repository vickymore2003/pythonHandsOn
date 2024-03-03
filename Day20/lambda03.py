def table(n):
    return lambda a:a*n

n=float(input("Enter any number : "))
b= table(n)
for i in range(1,31):
    print(n,"x",i,"=",b(i))