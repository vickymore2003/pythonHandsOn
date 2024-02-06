#program for star pattern
n = int(input("Enter no of rows: "))
for x in range(n+1):
    for y in range(x):
        print(y,end=" ")
    print()