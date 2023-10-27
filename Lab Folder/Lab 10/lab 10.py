#Create a Python Class for managing student details and marks.
#Define the class and implement the methods of the student class in a menu-driven program for different types of users

class student:
    def __init__(self):
        self.stuDetails ={}


    def StuDetails(self):

        self.dic1 ={
            "Name":name,
            "Regno": regno,
            "class": batch}
        
        self.dic2 = {
            "Math":math,
            "Stats":stats,
            "Excel":excel,
            "Python":python,
            "Total Marks":total,
            "percent":percentage
        }
        
        self.dic1["Marks"]=self.dic2
        self.stuDetails[regno] = self.dic1
        print(self.stuDetails)

    def view(self):
        flag = "True"
        for key in self.stuDetails.keys():
            if SearchReg == key:
                print(self.stuDetails[key])
                exit()
            else:
                flag = "False"
        if flag == "False":
            print("Student not found")

christ = student()


while True:
    
    print('1. Teacher')
    print('2. Student')
    choice_1 = int(input('Select your user type: '))
    if choice_1 == 1:
        while True:
            print('1. Input student details')
            print('2. View Database')

            choice_2 = int(input('Choose the funtion to perform: '))
            if choice_2==1:
                name = input("Enter the student name: ")
                regno = input("Enter the Register Number: ")
                batch = input("Enter the batch: ")
                math = int(input("Enter the Maths mark ot of 100: ")) 
                stats = int(input("Enter the Stats mark ot of 100: "))  
                excel = int(input("Enter the excel mark ot of 100: ")) 
                python = int(input("Enter the python mark ot of 100: "))
                total = math + stats + excel + python
                percentage = total/400
                christ.StuDetails() 

            elif choice_2==2:
                SearchReg = input("Enter the register number of searching student: ")
                christ.view()

            else:
                print("Thank you!")
                break
                
    elif choice_1 ==2:
        print('1. View Database')

        while True:
            choice_3 = int(input('Choose the funtion to perform: '))
            if choice_3 ==1:
                SearchReg = input("Enter the register number of searching student: ")
                christ.view()
            else:
                break
    else:
        exit()
            


    
        


        
        
    

    

