
def print_rectangle(rows, columns) :
     
    for i in range(1, rows+1) : #i iterates rows
        for j in range(1, columns+1) : #j iterates columns
            if (i == 1 or i == rows or
                j == 1 or j == columns):
                print(" \u2764\uFE0F", end="") 
            elif (i == 2 and j == 2):
                print("   welcome to the snakes cafe ", end="")           
            elif (i == 3 and j == 2):
                print("   Please see our menu bellow ", end="")
            elif(i==4 and j==2):
                print("  "*(columns-2), end="")
            elif (i == 5 and j == 2):
                print('  To quit anytime, type "quit"', end="")
            
        print() #new line at end

def print_menu(columns):
    print("\n  Appetizers: ")
    print(" " + "-"*columns*2)
    print("  Wings\n  Yalanji\n  Spring Rolls\n")
    print("\n  Entrees: ")
    print(" " + "-"*columns*2)
    print("  Salmon\n  Steak\n  Meat Tornado\n  A Literal Garden\n")
    print("\n  Desserts: ")
    print(" " + "-"*columns*2)
    print("  Ice Cream\n  Cookies\n  Apple Pie\n")
    print("\n  Drinks: ")
    print(" " + "-"*columns*2)
    print("  Water\n  PEPSI\n  Tea\n")

def take_order():
    user_orders = []
    rows = 3
    columns = 17
    for i in range(1, rows+1) : #i iterates rows
        for j in range(1, columns+1) : #j iterates columns
            if (i == 1 or i == rows or
                j == 1 or j == columns):
                print(" \u2764\uFE0F", end="") 
            elif (i == 2 and j == 2):
                print(" What would you like to order?", end="")
        print()
    wingsCounter = 0
    springCounter =0
    yalanjiCounter=0
    salmonCounter =0
    steakCounter =0
    meatCounter =0
    gardenCounter =0
    iceCounter =0
    cookieCounter =0
    pieCounter =0
    waterCounter =0
    pepsiCounter =0
    teaCounter =0

    while(True):

        order =input(">")
        if(order.lower() == "quit"):
            print("  Your order is: " + str(user_orders) + "\n  Thank you for visiting us!")
            break
        else:
            if(order.lower() == "wings"):
                wingsCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(wingsCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "yalanji"):
                yalanjiCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(yalanjiCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "spring rolls"):
                springCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(springCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "salmon"):
                salmonCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(salmonCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "steak"):
                steakCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(steakCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "meat tornado"):
                meatCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(meatCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "a literal garden"):
                gardenCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(gardenCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
             
            elif(order.lower() == "ice cream"):
                iceCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(iceCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "cookies"):
                cookieCounter+=1
                user_orders.append(order)
                print("\n you cheeky little cookie monster :) \n")
                print("\n \u2764\uFE0F " + str(cookieCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "apple pie"):
                pieCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(pieCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "water"):
                waterCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(waterCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "pepsi"):
                pepsiCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(pepsiCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
            
            elif(order.lower() == "tea"):
                teaCounter+=1
                user_orders.append(order)
                print("\n \u2764\uFE0F " + str(teaCounter) + " order of " + order + " added \u2764\uFE0F\n  Do you want anything else?\n")
   
            else:
                print("Item unavailable, did you make a mistake? \n")

rows = 6
columns = 17
print_rectangle(rows, columns)
print_menu(columns)
take_order()
