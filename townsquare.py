#This file is the structure of the town square

import TextBasedAdventureFunctions

def ragni_square():
    city = ("Ragni")
    print ("Welcome to Ragni!")
    TextBasedAdventureFunctions.blank_line(2)
    print ("----------------------------------------------")
    print ("Here's a list of where you can go in Ragni:")
    print ("1. Weapons Shop")
    print ("2. Armor Shop")
    print ("3. Bank")
    print ("4. Potion Merchanct")
    print ("5. Quest Board")
    print ("6. The Map")
    print ("----------------------------------------------")
    TextBasedAdventureFunctions.blank_line(2)

    place = int(input("Where would you like to go in Ragni? "))
    if place == 1:
        TextBasedAdventureFunctions.weapons_shop(city)


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
