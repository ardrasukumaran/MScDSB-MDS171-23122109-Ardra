#Creating module of our kwn
class student:
    def __init__(self,name,phone):#we use init method to initialise the data members
        self.name = name
        self.phone = phone
    
    def printStudent(self):
        print(self.name,self.phone)
        