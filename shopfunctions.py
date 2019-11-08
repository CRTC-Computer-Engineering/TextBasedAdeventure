import TextBasedAdventureFunctions
import townsquare

store = ()
balance = 10

class ragni_armor_shop():
    def __init__ (self):
        self.item1 = ("10G - Tattered Leather Chestplate")
        self.item2 = ("2G  - Tattered Leather Helm")
        self.item3 = ("3G  - Tattered Leather Shoes")
        self.item4 = ("6G  - Tattered Leather Pants")
        self.item5 = ("8G  - Cracked Barrel Top")
    def print_all_armor_ragni(self):
        print ("1. " + str(self.item1))
        print ("2. " + str(self.item2))
        print ("3. " + str(self.item3))
        print ("4. " + str(self.item4))
        print ("5. " + str(self.item5))

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
    while True:
        if city == ("Ragni"):
            input_ragni_armor_shop = int(input("Pick an action: "))
            global balance
            if input_ragni_armor_shop == 1:
                store = ragni_armor_shop()
                store.print_all_armor_ragni()
                purchase = int(input("Which item catches your eye? "))
                if purchase == 1:
                    if balance >= 10:
                        balance = balance - 10
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You bought the Tattered Leather Chestplate!")
                        TextBasedAdventureFunctions.blank_line(1)
                    else:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You cannot afford this item!")
                        TextBasedAdventureFunctions.blank_line(1)
                        continue
                elif purchase == 2:
                    if balance >= 2:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You bought the Tattered Leather Helm!")
                        TextBasedAdventureFunctions.blank_line(1)
                        continue
                    else:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You cannot afford this item!")
                        TextBasedAdventureFunctions.blank_line(1)
                        continue
                elif purchase == 3:
                    if balance >= 3:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You bought the Tattered Leather Shoes!")
                        TextBasedAdventureFunctions.blank_line(1)
                    else:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You cannot afford this item!")
                        TextBasedAdventureFunctions.blank_line(1)
                        continue
                elif purchase == 4:
                    if balance >= 6:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You bought the Tattered Leather Pants!")
                        TextBasedAdventureFunctions.blank_line(1)
                    else:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You cannot afford this item!")
                        TextBasedAdventureFunctions.blank_line(1)
                        continue
                elif purchase == 5:
                    if balance >= 8:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You bought the Cracked Barrel Top!")
                        TextBasedAdventureFunctions.blank_line(1)
                    else:
                        TextBasedAdventureFunctions.blank_line(1)
                        print ("You cannot afford this item!")
                        TextBasedAdventureFunctions.blank_line(1)
                        continue
                elif purchase == 6:
                    armor_shop(city)

            elif input_ragni_armor_shop == 2:
                print ("Do you think I'm made of money?! Get lost!")
                armor_shop(city)
            elif input_ragni_armor_shop == 3:
                continue
    else:
        print ("")
