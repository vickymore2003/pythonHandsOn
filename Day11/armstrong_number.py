# Program for armstong
a = int(input("Enter a number : "))
b = a
sum = 0
power = len(str(b))
print(power)
while a != 0:
    r=a%10
    sum=sum + r**power
    a=int(a/10)
if sum==b:
    print("Armstrong")
else:
    print("No Armstrong")