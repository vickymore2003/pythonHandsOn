str="Hello World"

#len to get the length of string
print(len(str)) 

#str.lower() converts the string to lower case
print(str.lower()) 

#str.upper() converts the string to upper case
print(str.upper()) 

str1 = " Hell World "
#str.strip() removes the spaces from beg and end
print(str.strip())

#str.replace() will replace the char 
print(str.replace("H","Y"))

#str.split will replace the text
str1="Hello, World"
print(str1.split(","))

#in and not in keyword check if the string is present
x ="Wor" in str1
print(x)
x ="World" not in str1
print(x)

# '+' concatinate the string
str2="Hello"
str3="World"
str4 = str2+" "+str3
print(str4)

#format use to concat number with string
a = 24
b = "Hello your age is {}"
print(b.format(a))