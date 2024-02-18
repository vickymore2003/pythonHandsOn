#program for Prime Number using recursion
n=int(input("Enter any number: "))

def prime(n,i=2):
    if n<=2:
        return True if n==2 else False
    if n%i==0:
        return False
    if i*i>n:
        return True
    return prime(n,i+1)    

if prime(n):
    print("Prime Number")
else:
    print("Not a Prime")    
