#Create a petstore class where you have the details of pets available and their details.
#The class will have the methods
##-store a new pet details
## - search for a pet
## - sell a pet
## - list all pets

#Importing your petstore class, create a petStoreMain file, where you will implement a menu driven program
#for admin - who will manage the store and user who will see the pets and buy pets

class petStore:
    def __init__(self):
        self.pet ={

            "cat":[],
            "love birds": [],
            "puppy" : [],
            "fish": [],
            "dog": []
        }

    def petDetails(self):
        details = {}
        Type = input("Enter the Type of pet: ")
        breed = input("Enter the breed of pet: ")
        age = input("Enter the age of the pet:  ")
        colour = input("Enter the colour of the pet: ")
        rate = int(input("Enter the rate of the pet: "))
        details["Breed"] = breed
        details["Age"] = age
        details["Colour"] = colour
        details["Rate"] = rate

        for item in self.pet.keys():
            exist = True
            if Type == item:
                
                self.pet[item].append(details)
                break
            else:
                exist = False
        if exist == False:
            print("Pet is not available")

    
    
    def searchPet(self):
        searchName = input("Enter the type of the pet:  ").lower()

        for type in self.pet.keys():
            flag = True
            if type == searchName:
                print(self.pet[type])
                searchBreed = input("Enter the searching breed: ")
                for i in self.pet[type]:
                    for breed in i.keys():
                        if searchBreed == i[breed]:
                            print(i)
                            break

                break
            else:
                flag = False
        if flag == False:
            print("Pet not found")
    
    # def sellPet(self):
    #     sold= input("Enter the breed you want to sell: ")

shop1 = petStore()
#menu driven
while True:
    choice = int(input("enter your choice: "))

    if choice ==1:
        shop1.petDetails()
    if choice ==2:
        shop1.searchPet()
    if choice ==3:
        exit()



shop1 = petStore()
#shop1.newPet()
shop1.searchPet()

        
        
