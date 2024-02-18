#program of an armstrong using recurssion

n = int(input("Enter any number: "))
m=n
sum=0

def arms(n):
    global sum
    if n>0:
        r = n%10
        sum=sum+r**3
        n=arms(n//10)
    return sum

b=arms(n)
if b==m:
    print("Armstrong number")
else:
    print("Not an Armstrong number")