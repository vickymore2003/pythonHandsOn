a=int(input("Enter the first number : "))
b=int(input("Enter the secound number : "))
c=int(input("Enter the third number : "))
if a>b and a>c:
    print("a is largest")
elif b>c and b>a:
    print("b is largest")
else:
    print("c is largest")