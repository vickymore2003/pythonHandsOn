#Recusrion is process in which a fucntion calls itself again and again
# program to add n natural numbers

n=int(input("Enter any number = "))

def sum(n):
    if n<=1:
        return 1
    else:
        return n+sum(n-1)
    
print(sum(n))