#program using recussion for palindrom

a=int(input("Enter any number: "))
b=a
sum=0

def palin(a):
    global sum
    if a>0:
        r=a%10
        sum=sum*10+r
        a=palin(a//10)
    return sum
m=palin(a)
if m==b:
    print("Palindrom")
else:
    print("Not a Palindrom")