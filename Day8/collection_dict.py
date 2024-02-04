#Dictonary is collection data type which is unordered , changeble and indexed

mydict={"Name":"Sunny", "Age":25,"Address":"India"}
print (mydict)
print(mydict["Address"]) #using key
print(mydict.get("Name"))
mydict["Age"]=26        #update the key of dictonary
print (mydict)
print(len(mydict))
mydict["Dept"]="IT"     # add a new key and Value
print (mydict)
mydict.pop("Address")   #remove address
print (mydict)
mydict.popitem()        #remove last item
print (mydict)
mydict1=mydict.copy()
print(mydict1)
del mydict
print (mydict)
