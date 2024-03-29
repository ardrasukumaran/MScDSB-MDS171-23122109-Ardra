import random
import csv

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

    def asCSV(self):
        with open("expenseTracker.csv" , "w+") as csvfile:
            for item in self.expenseDict['income']:
                csvfile.write(str(item))
            for item in self.expenseDict['Expense']:
                 csvfile.write(str(item))
         


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
    print("5.Store the Details as CSV File")
    print("6. EXIT")


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
    elif choice ==5:
        myexpense.asCSV()
    elif choice == 6:
        exit()
    else:
        print("In valid choice")     


            