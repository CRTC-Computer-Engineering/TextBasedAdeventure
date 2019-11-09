import TextBasedAdventureFunctions
import townsquare
import shopinfo
import os
import items
import bank
import character_info

#Calling inventory from character_info
inventory = character_info.inventory
#Calling balance from character_info
balance = character_info.balance


store = ()


def armor_shop(city):
    TextBasedAdventureFunctions.blank_line(1)
    print ("Welcome to the " + city + " Armor shop!")
    print ("How can we help you today?")
    print ("""---------------------------------------------
1. Buy
2. Sell
3. Back
---------------------------------------------""")
    TextBasedAdventureFunctions.blank_line(1)
    if city == ("Ragni"):
        input_ragni_weapon_shop = int(input("Pick an action: "))
        global balance
        if input_ragni_weapon_shop == 1:
            store = shopinfo.ragni_armor_shop()
            store.print_all_armor_ragni()
            purchase = int(input("Which item catches your eye? "))
            if purchase == 1:
                if balance >= 10:
                    balance = balance - 10
                    TextBasedAdventureFunctions.blank_line(1)
                    print ("You bought the Tattered Leather Chestplate!")
                    TextBasedAdventureFunctions.blank_line(1)
                    inventory.append(items.Tattered_Leather_Chestplate)
                    itemname = inventory.Tattered_Leather_Chestplate.get("name")
                    print (itemname)
                    armor_shop(city)
                else:
                    TextBasedAdventureFunctions.blank_line(1)
                    print ("You cannot afford this item!")
                    TextBasedAdventureFunctions.blank_line(1)
                    armor_shop(city)
            elif purchase == 2:
                if balance >= 2:
                    TextBasedAdventureFunctions.blank_line(1)
                    print ("You bought the Tattered Leather Helm!")
                    TextBasedAdventureFunctions.blank_line(1)
                    armor_shop(city)
                else:
                    TextBasedAdventureFunctions.blank_line(1)
                    print ("You cannot afford this item!")
                    TextBasedAdventureFunctions.blank_line(1)
                    armor_shop(city)
            elif purchase == 3:
                if balance >= 3:
                    TextBasedAdventureFunctions.blank_line(1)
                    print ("You bought the Tattered Leather Shoes!")
                    TextBasedAdventureFunctions.blank_line(1)
                    armor_shop(city)
                else:
                    TextBasedAdventureFunctions.blank_line(1)
                    print ("You cannot afford this item!")
                    TextBasedAdventureFunctions.blank_line(1)
                    armor_shop(city)
            elif purchase == 4:
                if balance >= 6:
                    TextBasedAdventureFunctions.blank_line(1)
                    print ("You bought the Tattered Leather Pants!")
                    TextBasedAdventureFunctions.blank_line(1)
                    armor_shop(city)
                else:
                    TextBasedAdventureFunctions.blank_line(1)
                    print ("You cannot afford this item!")
                    TextBasedAdventureFunctions.blank_line(1)
                    armor_shop(city)
            elif purchase == 5:
                if balance >= 8:
                    TextBasedAdventureFunctions.blank_line(1)
                    print ("You bought the Cracked Barrel Top!")
                    TextBasedAdventureFunctions.blank_line(1)
                    armor_shop(city)
                else:
                    TextBasedAdventureFunctions.blank_line(1)
                    print ("You cannot afford this item!")
                    TextBasedAdventureFunctions.blank_line(1)
                    armor_shop(city)
            elif purchase == 6:
                armor_shop(city)

            elif input_ragni_weapon_shop == 2:
                print ("Do you think I'm made of money?! Get lost!")
                armor_shop(city)
            elif input_ragni_weapon_shop == 3:
                townsquare.ragni_square()

    elif city == ("Detlas"):
        print ("Detlas armor shop doesn't exist yet")

    elif city == ("Almuj"):
        print ("Almuj armor shop doesn't exist yet")

    elif city == ("Nemract"):
        print ("Nemract armor shop doesn't exist yet")

    elif city == ("Nesaak"):
        print ("Nesaak armor shop doesn't exist yet")

    elif city == ("Troms"):
        print ("Troms armor shop doesn't exist yet")

    elif city == ("Rymek"):
        print ("Rymek armor shop doesn't exist yet")

    else:
        print ("Something went very wrong. Darn.")




def weapon_shop(city):
    TextBasedAdventureFunctions.blank_line(1)
    print ("Welcome to the " + city + " Weapon shop!")
    print ("How can we help you today?")
    print ("""---------------------------------------------
1. Buy
2. Sell
3. Back
---------------------------------------------""")
    TextBasedAdventureFunctions.blank_line(1)
    while True:
        if city == ("Ragni"):
            input_ragni_weapon_shop = int(input("Pick an action: "))
            global balance
            if input_ragni_weapon_shop == 1:
                store = shopinfo.ragni_weapon_shop()
                store.print_all_weapons_ragni()
                purchase = int(input("Which item catches your eye? "))
                if purchase == 1:
                    if balance >= 15:
                        balance = balance - 15
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You bought the Spiky Stick!")
                        TextBasedAdventureFunctions.blank_line(1)
                        weapons_shop(city)
                    else:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You cannot afford this item!")
                        TextBasedAdventureFunctions.blank_line(1)
                        weapons_shop(city)
                elif purchase == 2:
                    if balance >= 15:
                        balance = balance - 15
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You bought the Sparkly Stick!")
                        TextBasedAdventureFunctions.blank_line(1)
                        weapons_shop(city)
                    else:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You cannot afford this item!")
                        TextBasedAdventureFunctions.blank_line(1)
                        continue
                elif purchase == 3:
                    if balance >= 15:
                        balance = balance - 15
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You bought the Sharp Spoon!")
                        TextBasedAdventureFunctions.blank_line(1)
                        weapons_shop(city)
                    else:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You cannot afford this item!")
                        TextBasedAdventureFunctions.blank_line(1)
                        weapons_shop(city)
                elif purchase == 4:
                    if balance >= 15:
                        balance = balance - 15
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You bought the Bendy Stick!")
                        TextBasedAdventureFunctions.blank_line(1)
                        weapons_shop(city)
                    else:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You cannot afford this item!")
                        TextBasedAdventureFunctions.blank_line(1)
                        armor_shop(city)
                elif purchase == 5:
                    armor_shop(city)

            elif input_ragni_weapon_shop == 2:
                print ("Do you think I'm made of money?! Get lost!")
                armor_shop(city)
            elif input_ragni_weapon_shop == 3:
                townsquare.ragni_square()
        elif city == ("Detlas"):
            print ("Detlas armor shop doesn't exist yet")

        elif city == ("Almuj"):
            print ("Almuj armor shop doesn't exist yet")

        elif city == ("Nemract"):
            print ("Nemract armor shop doesn't exist yet")

        elif city == ("Nesaak"):
            print ("Nesaak armor shop doesn't exist yet")

        elif city == ("Troms"):
            print ("Troms armor shop doesn't exist yet")

        elif city == ("Rymek"):
            print ("Rymek armor shop doesn't exist yet")

        else:
            print ("Something went very wrong. Darn.")
