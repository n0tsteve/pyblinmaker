__author__ = "Steve from Ukraine"

# import the math library for rounding down the portions
import math

# Ask the name of the user and define it as a variable
print("Hello! How can i call you?\n")
user_name = input("Your name: ")

# check if its not Vadim
if user_name.lower() == "vadim":
    while 2 > 1:
        print("Vadim Blyat!")

# tell the user that he has a nice name
print("What a nice name, " + user_name + "!")

# ask user for how much ingredients he have and store them in a variable
print("\nSo, how much milk you have? In litres, please! :)")
amountOfMilk = input("Amount of milk: ")
print("\nAnd how about eggs? ")
amountOfEggs = input("Amount of eggs: ")
print("\nAnd yeah, flour. How much you have? In kilograms, please! :)")
amountOfFlour = input("Amount of flour: ")

# set the minimum needed amount of all ingredients needed for oe portion of blins
minMilk = 0.2
minEggs = 1
minFlour = 0.1


# this function tells the user (or not) how many ingredients will he need for his portions of blins
def askforreceipt():
    while 2 > 1:
        print("Do i need to show you how many ingredients you need?")
        response = input("(y)es or (n)o? ")
        if response.lower() == "y":
            print("\nYou will need:")
            print(str(int(minEggs*portions)) + " egg(s)")
            print(str(float(minMilk*portions)) + " liters of milk")
            print(str(float(minFlour*portions)) + " kilograms of flour")
            exit()
            break
        elif response.lower() == "n":
            exit(0)
        else:
            print("Wrong answer! Try again, " + user_name)


# this function determines, and tells the end user, that what ingredients are insufficient
def fail(code):
    print("\nSorry, no blins today :(")
    if int(code) == 1:
        print("You have " + amountOfMilk + " litres, but you need " + str(minMilk) + " litres of milk.")
    elif int(code) == 2:
        print("You have " + amountOfFlour + " kilograms, but you need " + str(minFlour) + " kilograms of flour.")
    elif int(code) == 3:
        print("You have " + amountOfEggs + " eggs, but you need " + str(minEggs) + " eggs.")
    exit(1)


# check if user has enough ingredients
'''
TODO: make that thing with value error like with the eggs
'''
try:
    if float(amountOfMilk) >= float(minMilk):
        try:
            if float(amountOfFlour) >= float(minFlour):
                try:
                    if int(amountOfEggs) >= int(minEggs):
                        flour = float(amountOfFlour) / float(minFlour)
                        milk = float(amountOfMilk) / float(minMilk)
                        eggs = float(amountOfEggs) / float(minEggs)
                        portions = min(flour, milk, eggs)
                        result = math.floor(portions)
                        print("\nYou have enough ingredients for " + str(result) + " portion(s) of blins!")
                        print("Make them like your babushka did!")
                        askforreceipt()
                    else:
                        fail(3)
                except ValueError:
                    print("\nHow can you have THIS amount of EGGS? And how you want to cook something with it?")
            else:
                fail(2)
        except ValueError:
            print("\nHow can you have THIS amount of FLOUR? And how you want to cook something with it?")
    else:
        fail(1)
except ValueError:
    print("\nHow can you have THIS amount of MILK? And how you want to cook something with it?")
    exit()
