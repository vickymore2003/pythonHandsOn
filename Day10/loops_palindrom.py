a=int(input("Enter any number : "))
print("You have entered ",a)
b=a
sum=0
while a!=0:
    r = a%10
    sum= sum*10+r
    a=int(a/10)
# print (sum)
if sum==b:
    print("Number",b, "is palindrom")
else:
    print("Number",b, "is not palindrom")