#Create a sportMart class where you have inventory/shelf of items and order of customers
#create a csv file which will store your inventory details and order details
#With the help of file handling technique in python, read the files and create an object for trinity store
#and populate the inventory items and orders for the trinity object
#To make sure that you have added all the items in your file, use a display method to show your inventory and order history

import random

class sportMart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def GenOrderid(self):
        orderid = "OD"
        for i in range(1,4): #to get a 4 digit random orderID
            orderid = orderid+str(random.randint(i,9))#concatenating strings
        return orderid

    def createOrder(self,orderid,ItemName,Quantity,Price,Total):
        temp = {
            "orderid": orderid,
            "Item name": ItemName,
            "Qnty" : Quantity,
            "Price" : Price,
            "Total" : Total
        }

        self.orders[orderid] = temp

    def addInventory(self,productid,ProductName, Quantity,Price,Total):
        temp = {
            "Productid":productid,
            "ProductName": ProductName,
            "Qnty" : Quantity,
            "Price" : Price,
            "Total" : Total
        }
        self.inventory[productid] = temp

    def GenProductId(self):
        productid = "PD"
        for i in range(1,4): #to get a 4 digit random orderID
            productid = productid+str(random.randint(i,9))#concatenating strings
        return productid
    
    def printOrders(self):
        print(self.orders)

    def printInventory(self):
        print(self.inventory)
    


trinity = sportMart()
orders = open("OrderDetail.csv","r")
orders_header = orders.readline()
orders_orders = orders.readlines()
for item in orders_orders:
    temp = item.strip().split(',')
    trinity.createOrder(temp[0],temp[1],temp[2],temp[3],temp[4])
#trinity.printOrders()

# inventory = open("ProductDetails.csv")
# inventory_header = inventory.readline()
# inventory_product = inventory.readlines()
# for item in inventory_product:
#     temp = item.strip().split(',')
#     trinity.addInventory(temp[0],temp[1],temp[2],temp[3],temp[4])
# trinity.printInventory()

#Create a menu driven program that will
#1. create new orders and update the inventory accordingly
#2. Export the final data to the file

    
# new order
while True:
    choice = int(input("Enter your choice: "))

    if choice ==1:
        orderid = trinity.GenOrderid()
        order_item = input("Enter the Item anme")
        order_quantity = int(input("Enter the quantity"))
        order_price = int(input("Enter the price of item"))
        order_total = order_quantity*order_price
        prod_qnty = 
        trinity.createOrder(orderid,order_item,order_quantity,order_price,order_total)
    elif choice ==2:
        trinity.printOrders()
    else:
        exit()
    



