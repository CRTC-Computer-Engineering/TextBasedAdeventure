#This file is the structure of the town square

import TextBasedAdventureFunctions

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
        TextBasedAdventureFunctions.weapons_shop(city)
    elif place == 2:
        print ("")


def detlas_square():
    print ("")

def almuj_square():
    print ("")

def nemract_square():
    print ("")

def nessak_square():
    print ("")

def troms_square():
    print ("")

def rymek_sqaure():
    print ("")
