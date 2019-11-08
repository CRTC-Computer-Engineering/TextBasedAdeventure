import AdventureMaps
import classes

#Creating info for mage class
user_niche = ()
user_object = ()
store = ()
class Mage():
    def __init__ (self):
        self.name = ("Mage")
        self.health = 100
        self.mana = 20
        self.attack = 10
        self.defence = 10
    def print_all_things(self):
        print ("Class: " + str(self.name))
        print ("Health: " + str(self.health))
        print ("Mana: " + str(self.mana))
        print ("Attack: " + str(self.attack))
        print ("Defence: " + str(self.defence))


#Info for archer class
class Archer():
    def __init__ (self):
        self.name = ("Archer")
        self.health = 150
        self.mana = 12
        self.attack = 14
        self.defence = 14
    def print_all_things(self):
        print ("Class: " + str(self.name))
        print ("Health: " + str(self.health))
        print ("Mana: " + str(self.mana))
        print ("Attack: " + str(self.attack))
        print ("Defence: " + str(self.defence))

#Info for assassin class
class Assassin():
    def __init__ (self):
        self.name = ("Assassin")
        self.health = 75
        self.mana = 15
        self.attack = 15
        self.defence = 7
    def print_all_things(self):
        print ("Class: " + str(self.name))
        print ("Health: " + str(self.health))
        print ("Mana: " + str(self.mana))
        print ("Attack: " + str(self.attack))
        print ("Defence: " + str(self.defence))


#Info for warrior class
class Warrior():
    def __init__ (self):
        self.name = ("Warrior")
        self.health = 175
        self.mana = 8
        self.attack = 175
        self.defence = 150
    def print_all_things(self):
        print ("Class: " + str(self.name))
        print ("Health: " + str(self.health))
        print ("Mana: " + str(self.mana))
        print ("Attack: " + str(self.attack))
        print ("Defence: " + str(self.defence))

#Info for ragni armor shop
class ragni_armor_shop():
    def __init__ (self):
        self.item1 = ("10G - Tattered Leather Chestplate")
        self.item2 = ("2G  - Tattered Leather Helm")
        self.item3 = ("3G  - Tattered Leather Shoes")
        self.item4 = ("6G  - Tattered Leather Pants")
        self.item5 = ("8G  - Cracked Barrel Top")
    def print_all_armor_ragni(self):
        print ("---------------------------------------------")
        print ("1. " + str(self.item1))
        print ("2. " + str(self.item2))
        print ("3. " + str(self.item3))
        print ("4. " + str(self.item4))
        print ("5. " + str(self.item5))
        print ("6. Back")
        print ("---------------------------------------------")

#Used to print number of desired blank lines
def blank_line(lines):
    for i in range(lines):
        print ("")



#Used for inspecting classes inside of the class selection function
def look_at_class():
    while True:
        inspect_class = input("What class would you like to inspect?")
        if inspect_class == ("mage"):
            user_object = Mage()
            user_object.print_all_things()
            print ("Type back to choose a class!")
        elif inspect_class == ("archer"):
            user_object = Archer()
            user_object.print_all_things()
            print ("Type back to choose a class!")
        elif inspect_class == ("assassin"):
            user_object = Assassin()
            user_object.print_all_things()
            print ("Type back to choose a class!")
        elif inspect_class == ("warrior"):
            user_object = Warrior()
            user_object.print_all_things()
            print ("Type back to choose a class!")
        elif inspect_class == ("back"):
            break
        else:
            print ("That is not a valid option!")
            continue



#Used to choose a class at the beginning of the game
def choose_class():
    global user_niche
    global user_object
    while True:
        niche = input("What class would you like? Or would you like to inspect a class?")
        if niche == ("mage"):
            print ("You are now a Mage!")
            user_object = Mage()
            user_niche = ("mage")
            blank_line(2)
            break
        elif niche == ("archer"):
            print ("You are now an Archer!")
            user_object = Archer()
            user_niche = ("archer")
            blank_line(2)
            break
        elif niche == ("assassin"):
            print ("You are now an Assassin!")
            user_object = Assassin()
            user_niche = ("assassin")
            blank_line(2)
            break
        elif niche == ("warrior"):
            print ("You are now a Warrior!")
            user_object = Warrior()
            user_niche = ("warrior")
            blank_line(2)
            break
        elif niche == ("inspect"):
            look_at_class()


def print_stats():
    user_object.print_all_things()

def current_map():
    print ("")

def weapons_shop(city):
    print ("Welcome to the " + city + " weapon shop!")
    blank_line(1)
    print ("How can we help you today?")
    print ("""---------------------------------------------
1. Buy
2. Sell
3. Back
---------------------------------------------""")
    blank_line(1)
    input_ragni_armor_shop = int(input("Pick and action: "))
    while True:
        if input_ragni_armor_shop == 1:
            store = ragni_armor_shop()
            store.print_all_armor_ragni()
            purchase = int(input("Which item catches your eye? "))
            if purchase == 1:
                    ("ok")
        elif input_ragni_armor_shop == 2:
            print ("Do you think I'm made of money?! Get lost!")
            continue
        elif input_ragni_armor_shop == 3:
            continue
