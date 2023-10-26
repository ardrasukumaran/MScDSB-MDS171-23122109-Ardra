listNames = [] #Empty list to store the names

#store a name to list
def storeName(name):
    name = name.strip().title()
    if name in listNames:
        return False
    else:
        listNames.append(name)
        return True

#To list all names

def listNames():
    print("-",*30) #printing - 30 times
    for name in listNames:
        print(name)
    print("-"*30)

#Function to search a name
def searchName(name):
    name = name.strip().title()
    flag = False
    for item in listNames:
        if name == item:
            flag = True
    
    if flag == True:
        print("Name exist in the list")
    else:
        print("Name Doesnot Exist")




while True:
    print("Menu Options")
    print("*"*30)
    print("1. Enter a Name")
    print("2. search a Name")
    print("3. List all Names")
    print("4.Exit")

    choice = int(input("Enter your choice: "))
       
if choice == 1:
    userInp = input("Enter the name")
    retVal = storeName(userInp)
    if retVal == True:
        print("Name added successfully")
    else:
        print("Name exists in the list")
elif choice == 2:
    userInp = input("Enter the name to be searched")
    searchName(userInp)
elif choice == 3:
    printNames()
elif choice ==4:
    exit

