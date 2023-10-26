class PhoneDir():

    def __init__(self):
        self.dic2 ={}

    def add(self):
        global Ph
        Ph="Ph"
        name = input("enter the Name: ")
        No = input("Enter the no: ")
        place = input("Enter the place")
        self.dic3 = {
            "Name":name,
            "Ph": No,
            "place":place
        }
        self.dic2[No]=self.dic3
        print(self.dic2)
    
    # def edit(self):

    #     editNo = input("Enter the number: ")
    #     for key in self.dic2.keys():
    #         flag = True
    #         if editNo == key:
    #             newName = input("Enter the Newname: ")
    #             newPh = input("Enter the Newph: ")
    #             newPlace = input("Enter the Newplace: ")
    #             self.dic2[key]["Name"] = newName
    #             self.dic2[key]["Ph"] = newPh
    #             self.dic2[key]["place"] = newPlace
    #             print(self.dic2)
    #             break
    #         else:
    #             flag = False
    #     if flag == False:
    #         print(self.dic2)

    def edited(self):
        enter = input("Enter the attribute to be changed: ")
        if enter == "name":
            newName = input("Enter the edited name: ")
            self.dic2["Ph"]["Name"] = newName
        elif enter == "phone":
            newPhone = input("Enter the edited ph: ")
            self.dic2["Ph"]["Ph"] = newPhone
        elif enter == "place":
            newPlace = input("Enter the edited place: ")
            self.dic2["Ph"]["place"] = newPlace
        print("Edited list is: ", self.dic2)       


    
    def delete(self):
        delNo = input("Enter the no to be deleted: ")
        self.dic2.pop(delNo)
        print(self.dic2)
    
    def searchItem(self):
        searchName = input("Enter the ph")
        for key in self.dic2.keys():
            flag = True
            if searchName == key:
                print(self.dic2[key])
                break
            else:
                flag = False
        if flag == False:
            print("Search not found")

a = PhoneDir()

#Menu Driven
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        a.add()
    elif choice == 2:
        a.edited()
    elif choice == 3:
        a.delete()
    elif choice == 4:
        a.searchItem()
    elif choice == 5:
        exit()
    else:
        print("Invalid choice")



    


