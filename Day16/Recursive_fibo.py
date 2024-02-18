#Program to print fibbonacci sung recurssion


def fibbo(n):
    if n<=1:
        return 1
    else:
        return(fibbo(n-1)+fibbo(n-2))

n=int(input("Enter any number: "))
for x in range(n):
    print(fibbo(x),end="\t")