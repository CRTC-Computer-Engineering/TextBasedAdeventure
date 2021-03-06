import AdventureMaps
import classes

#Creating info for mage class
user_niche = ()
user_object = ()
store = ()
balance = 10
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
        print ("""---------------------------------------------
1. Mage
2. Archer
3. Assassin
4. Warrior
5. Back
---------------------------------------------""")
        blank_line(3)
        inspect_class = int(input("What class would you like to inspect?"))
        if inspect_class == 1:
            user_object = Mage()
            user_object.print_all_things()
            print ("Press 5 to go back.")
            blank_line(2)
        elif inspect_class == 2:
            user_object = Archer()
            user_object.print_all_things()
            print ("Press 5 to go back.")
            blank_line(2)
        elif inspect_class == 3:
            user_object = Assassin()
            user_object.print_all_things()
            print ("Press 5 to go back.")
            blank_line(2)
        elif inspect_class == 4:
            user_object = Warrior()
            user_object.print_all_things()
            print ("Press 5 to go back.")
            blank_line(2)
        elif inspect_class == 5:
            choose_class()
        else:
            print ("That is not a valid option!")
            continue



#Used to choose a class at the beginning of the game
def choose_class():
    while True:
        print ("""---------------------------------------------
1. Mage
2. Archer
3. Assassin
4. Warrior
---------------------------------------------""")
        global user_niche
        global user_object
        
        niche = input("What class would you like?")
        if niche == ("1"):
            print ("You are now a Mage!")
            user_object = Mage()
            user_niche = ("mage")
            blank_line(2)
            break
        elif niche == ("2"):
            print ("You are now an Archer!")
            user_object = Archer()
            user_niche = ("archer")
            blank_line(2)
            break
        elif niche == ("3"):
            print ("You are now an Assassin!")
            user_object = Assassin()
            user_niche = ("assassin")
            blank_line(2)
            break
        elif niche == ("4"):
            print ("You are now a Warrior!")
            user_object = Warrior()
            user_niche = ("warrior")
            blank_line(2)
            break
        else:
            print ("That is not a valid input.")
            continue


def print_stats():
    user_object.print_all_things()

def current_map():
    print ("")
