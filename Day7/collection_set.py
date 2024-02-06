# Set is collection data type which is unindex adn unordered. unindex mean element cannot be accessed by index value

myset={"mouse","keyboard","monitor","cpu","usb"}
print(myset)
print("monitor" in myset)
myset.add("printer")
print(myset)

myset.update(["scanner","camera","drive","monitor"])  #Add more than one element
print(myset)
print(len(myset))

myset.remove("cpu") #if content is available then it will through error
print(myset)

myset.discard("usb1")#if content is available then it will not through error
print(myset)
myset.clear() #clear the content
print(myset)

x={"a","b","c"}
y={1,2,3}
z=x.union(y)  
print(z)


del myset
print(myset)