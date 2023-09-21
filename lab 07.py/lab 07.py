import csv
# #class is the keyword. __init__ is a member function to initialise the data entries in the class.
# #self.name and self.students are data members/properties or attributes of the class

# class MSCDSB:

#     def __init__(self):
#         self.name = "MSc DS B"
#         self.students = ["A","B","C"]
    
#     def printStudents(): #Another member function
#         for students in self.students:
#             print(student)

    

# ##to have mltiple copies of the class we need to call the class
# #to access the object inside the class

# obj = MSCDSB()
# print(obj.name)
# print(obj.students)
# obj.printStudents()

# class car:

#     def __init__(self,mfg,mdl,yr): 
#         self.manufacturer = mfg
#         self.model = mdl
#         self.year = yr

# bmw = car("BMW","F Series","2020")
# print(bmw.manufacturer)

# ferari = car("Ferari","A Series","2023")
# print(ferari.model)



#Create a class resturant that accepts
#itemName and Qnty ad input
#Inside the class you are having the item
#and its price(unit price) as a dictionary
#Create a function calcute cost
#that prints the itemname, qnty and price

#Create a class resturant that accepts
#itemName and Qnty ad input
# class resturant:

#     def __init__(self,itemName,Qnty):
#         self.itemName = itemName
#         self.Qnty = Qnty
#         self.menuItems = {
#             "Rice":30,
#             "Chicken":100,
#             "Dal": 40,
#             "Chappathi":15,
    
#         }

#     def totalCost(self):
#         print("Total Cost of the order")
#         print("Item\t:",self.itemName)
#         print("Qnty\t:",self.Qnty)
#         total = self.Qnty*self.menuItems[self.itemName]
#         print("Total\t:",total)

# order = resturant("Chicken",10)
# order.totalCost()

# class resturant:


#     menuList = {}
#     def __init__(self,itemName,Qnty):
#         self.itemName = itemName
#         self.Qnty = Qnty
#         self.menuItems ={
#             "Rice":40,
#             "Chicken":100,
#             "Dal": 40,
#             "Chappathi":15,
    
#         }

#     def totalCost(self):
#         print("Total Cost of the order")
#         print("Item\t:",self.itemName)
#         print("Qnty\t:",self.Qnty)
#         total = self.Qnty*self.menuItems[self.itemName]
#         print("Total\t:",total)

# order = resturant("Chicken",10)
# order.totalCost()

# Define a class expense Tracker that stores the
# expenses and income in a dictionary
# implement the method to
# - store the transaction
# - view the transaction
# - calculate the total expense/income

class expenseTracker:

    def __init__(self):
        self.expenseDict = {
            "income": [],
            "Expense": [],
        }

    def store_transactions(self,type,amnt,category,date,details):
            trans = {
                "Amount":amnt,
                "Category":category,
                "Date": date,
                "Details": details,
            }
            if type =="income":
                self.expenseDict['income'].append(trans)
            else:
                self.expenseDict['Expense'].append(trans)

    def view_transactions(self):
            print("your income:")
            for item in self.expenseDict['income']:
                print(item)
            print("your expense:")
            for item in self.expenseDict['Expense']:
                print(item)
    def calculate_transactions(self):
            total_income = 0
            for item in self.expenseDict['income']:
                total_income = total_income+item["Amount"]
            print("Total Income\t:\t",total_income)

            total_expense = 0
            for item in self.expenseDict['Expense']:
                total_expense = total_expense+item["Amount"]
            print("Total Expense\t:\t",total_expense)


#define a menu that will let users to enter expense, view expenses
#or income, get totals in each and exit from the program

def collectionInput():
    amt = int(input("Enter the amount:"))
    category = input("Enter the category:")
    date = input("Enter the date DD/MM/YYYY:")
    details = input("Enter the description:")
    return amt, category, date, details

myexpense = expenseTracker()

while True:
    print("_______MY EXPENSE______")
    print("1. Record Income")
    print("2. Record Expense")
    print("3.View Records")
    print("4. View my Spendings")
    print("5.Exit")

    field_names = ['Amount','Category','Date','Details']
    with open("ExpenseTracker.csv","w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(trans)

    choice = int(input("Enter your choice:").strip())

    if choice == 1:
        print("Enter the details of income")
        amt, category, date, details = collectionInput()
        myexpense.store_transactions("income", amt, category, date, details)
    elif choice == 2:
        print("Enter the details of expense")
        amt, category, date, details = collectionInput()
        myexpense.store_transactions("Expense", amt, category, date, details)
    elif choice == 3:
        myexpense.view_transactions()
    elif choice == 4:
        myexpense.calculate_transactions()
    elif choice == 5:
        exit()
    else:
        print("In valid choice")


# create a method in the class
# to export the details in the form of csv
# add export details to a file in the menu options       


            