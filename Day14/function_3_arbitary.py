def getName(*name): #if variable count is not known add * in front of vatiable
    print("the name is "+name[2])

def getName(name1, name2,name3,name4):
    print("The name is "+ name2)

def getName2(**name):
    print("The name is "+ name["name4"])

getName("Sachin","Saurav","Anil","Zaheer")

getName(name1="Sachin",name2="Saurav",name3="Anil",name4="Zaheer")

getName2(name1="Sachin",name2="Saurav",name3="Anil",name4="Zaheer")
