a = int(input("Enter the number : "))
first = 0
secound=1
for x in range(a):
    if x<=1:
        print(x,end="\t")
    else:
        fib=first+secound
        print(fib,end="\t")
        first =secound
        secound=fib
