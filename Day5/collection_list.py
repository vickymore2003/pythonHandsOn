#List: It is collection of ordered and changeable , Dup elements are allowed
mylist=["mouse","keyboard","monitor","printer","scanner","usb"]
print(mylist)
print(mylist[0])
print(mylist[2:5]) #last element is not displayed
print(mylist[:5])
print(mylist[2:])
print(mylist[-2])
print(mylist[-4:-2]) #last element is not displayed
mylist[1]="CPU" #replace element in list
print(mylist)
print(len(mylist))
mylist.append("keyboard") #add item at last 
print(mylist)
mylist.insert(2,"camera") #inser an item at defined index
print(mylist)
mylist.remove("keyboard") #remove the defined element
print(mylist)
mylist.clear()      #clear the elements of list
print(mylist)

mylist1=["a","b","c"]
mylist2=["1","2","3"]
mylist3=mylist1+mylist2     #combine 2 list together
print(mylist3)
del mylist3      # delete the list
print(mylist3)
