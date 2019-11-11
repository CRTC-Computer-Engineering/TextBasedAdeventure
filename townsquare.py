#This file is the structure of the town square
import TextBasedAdventureFunctions
import shopfunctions

def ragni_square():
    city = ("Ragni")
    print ("Welcome to Ragni!")
    TextBasedAdventureFunctions.blank_line(2)
    print ("""---------------------------------------------
Here's a list of where you can go in Ragni:
1. Weapons Shop
2. Armor Shop
3. Bank
4. Potion Merchant
5. Quest Board
6. The Map
---------------------------------------------""")
    TextBasedAdventureFunctions.blank_line(2)

    place = int(input("Where would you like to go in Ragni? "))
    if place == 1:
        shopfunctions.weapons_shop(city)
    elif place == 2:
        shopfunctions.armor_shop(city)
    elif place == 3:
        print ("Money is no")
        ragni_square()
    elif place == 4:
        print ("Sorry No Pot")
        ragni_square()
    elif place == 5:
        print ("Questn't")
        ragni_square()
    elif place == 6:
        print ("""Okay its Childish Gamino homegirl drop it like the NASDAQ""")
        ragni_square()
    else:
        print int("That is not a valid option.")

def detlas_square():
    city = ("Detlas")
    print ("Welcome to Detlas!")
    TextBasedAdventureFunctions.blank_line(2)
    print ("""---------------------------------------------
Here's a list of where you can go in Detlas:
1. Weapons Shop
2. Armor Shop
3. Bank
4. Potion Merchant
5. Enchanter
6. Quest Board
7. The Map
---------------------------------------------""")
    TextBasedAdventureFunctions.blank_line(2)

    place = int(input("Where would you like to go in Detlas? "))
    if place == 1:
        shopfunctions.weapons_shop(city)
    elif place == 2:
        shopfunctions.armor_shop(city)
    elif place == 3:
        print ("Money is no")
        detlas_square()
    elif place == 4:
        print ("Sorry No Pot")
        detlas_square()
    elif place == 5:
        print ("Enchanter is out to lunch")
        detlas_square()
    elif place == 6:
        print ("Questn't")
        detlas_square()
    elif place == 7:
        print ("""Okay its Childish Gamino homegirl drop it like the NASDAQ""")
        detlas_square()
def almuj_square():
    print ("")

def nemract_square():
    print ("")

def nesaak_square():
    print ("")

def troms_square():
    print ("")

def rymek_sqaure():
    print ("")
