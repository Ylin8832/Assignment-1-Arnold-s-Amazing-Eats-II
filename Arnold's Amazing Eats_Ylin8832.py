# Name:                     Arnold's Amazing Eats
# Author:                   Yunfeng Lin
# Date Created:             February 5, 2023
# Date Last Modified:       February 7, 2023

# Greetings to the customer and an explanation about this program.
print("\t\t!!!Welcome to Arnold's Eats!!!" , "\n\nThis program helps us to receive customer's order rapidly and accurately." , 
      "-------------------------------------------------------------------------" , sep="\n")
print("\nPlease enter you first name and last name.")
firstName = input("First name: ") # Receive input from the user, then store the customer's first name into the variable [firstName].
lastName = input("Last name: ") # Receive input from the user, then store the customer's last name into the variable [lastName].

# Prompt user to input address and phone number and store each value to the respective variable.
print("Please enter your delivery address.") 
st_Num = input("Street Number: ") 
st_Name = input("Stree Name: ")
unit_Num = input("Enter if applicable (leave blank if none): ")
city = input("Enter your city: ")
province = input("Enter your province: ")
post_Code = input("Enter your postal code: ")
special_Inst = input("Sepecial instructions on your delivery address: ")
phone_Num = input("Enter your phone number: ")

# Display the message to verify the address and phone number that the user has input.
print("-----------------------------")
print("\nHi" , firstName, "," , "you are all set!" , "\n\nYour address is: " , st_Num + " " + st_Name + " " + "Street" + "," + unit_Num + " " + city + ", " + province + ". " + post_Code , "***Note:" , special_Inst , "***" , "\nYour Phone number is: " + phone_Num)

# Display the menu
print("\nPlease select the meal from the menu","\n\t\t--------MENU---------",
      "\n\t1. Teriyaki Chiken meal   $15.50","\n\t2. Fried Chicken meal     $14.20")

meal_1Name = ("Teriyaki Chicken meal")
meal_2Name = ("Fried Chicken meal")
price1 = 15.50
price2 = 14.50

# Function to decide student or not.
def studentDiscount():
    student = input("Are you a student? [y/n]: ")

    while True: 
        if student.upper() == "Y": 
            student = True
            break
        elif student.upper() == "N":
            student = False
            break
        else:
            student = input("Please enter a valid input [y/n]: ")
    return(student)

# Function to calculate the student discount.
def sum(price1, student): 
    subtotal1 = int(meal_Qty) * price1
    print("\n\t\t\tItem","\tItem","\nOrder","\t\t\tAmt","\tPrice","\t\tTotal",
      "\n-------------","\t\t----","\t-----","\t     ---------","\n",meal_1Name,
      "\t2","\t$meal_1","\t\t$21.70","\n")

    if student:
        discountStud = subtotal1 * 0.1 # Calculate the discount rate and pass the value to the variable [discountStud]
        print("10% student saving","\t\t\t\t-${0:.2f}".format(discountStud))

    hst = subtotal1 * 0.13 # calculate the HST rate and pass the value to the variable [hst]

    print("\n\t\t\t\tSub Total",
        "\t$",subtotal1,"\n\t\t\t\tTax (13%)","\t $", hst,"\n\t\t\t\t\t\t-------","\n\t\t\t\tTotal","\t\t$22.07")

# Enter either No. 1 or 2 to select the menu and display selected menu and price.
# Enter the quantity to continue ordering and press either y or n to confirm.
# If there's no value (y or n) is entered, will go into loop.
while True: 
    meal_Type = input("\nEnter the meal number 1 or 2: ")

    if meal_Type == "1": 
        print("Your meal is" , "{0} ${1:.2f}".format(meal_1Name,price1)) 
        meal_Qty = input("Enter the quantity of your meal: ")
   
    elif meal_Type == "2":
        print("Your meal is" , "{0} ${1:.2f}".format(meal_2Name,price2))
        meal_Qty = input("Enter the quantity of your meal: ")
  
    confirmation = input("Please enter y for [Yes] or n for [No] to confirm your order: ")
    if confirmation.upper() == "Y": 
        isStudent = studentDiscount()
        print("\n\tThank you! Please confirm your receipt.")
        if meal_Type == "1":
            sum(price1, isStudent)
        elif meal_Type == "2":
            sum(price2, isStudent)
        break
    elif confirmation.upper() == "N":
        print("Sorry, please try again.")
        meal_Type = 0
