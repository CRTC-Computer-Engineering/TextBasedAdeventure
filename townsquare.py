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
    elif place == 4:
        print ("Sorry No Pot")
    elif place == 5:
        print ("Questn't")
    elif place == 6:
        print ("""Okay its Childish Gamino homegirl drop it like the NASDAQ
Move white girls like there's coke up my ass crack
Move black girls trust me fuck it ill do either
I love pussy i love bitches dude i should running Peeta""")


def detlas_square():
    print ("")

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
