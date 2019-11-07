#Creating info for mage class
user_niche = ()
user_object = ()
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
        selt.defence = 7
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



#Used to print number of desired blank lines
def blank_line(lines):
    for i in range(lines):
        print ("")


#Used for inspecting classes inside of the class selection function
def look_at_class():
    inspect_class = input("What class would you like to inspect?")
    while (True):
        if inspect_class == ("mage"):
            user_object = Mage()
            user_object.print_all_things()
            yesno = input("Would you like to inspect another class?(y/n) ")
            if yesno == ("y"):
                continue
            elif yesno == ("n"):
                break
            else:
                print ("y and n are the only valid choices.")
        elif inspect_class == ("archer"):
            user_object = Archer()
            user_object.print_all_things()
            yesno = input("Would you like to inspect another class?(y/n) ")
            if yesno == ("y"):
                continue
            elif yesno == ("n"):
                break
            else:
                print ("y and n are the only valid choices.")

#Used to choose a class at the beginning of the game
def choose_class():
    global user_niche
    global user_object
    while True:
        niche = input("What class would you like? Or would you like to inspect a class?")
        if niche == ("mage"):
            print ("You are now a mage!")
            user_object = classes.Mage()
            user_niche = ("mage")
            break
        elif niche == ("archer"):
            print ("You are now an archer!")

            user_niche = ("archer")
            break
        elif niche == ("assassin"):
            print ("You are now an assassin!")

            user_niche = ("assassin")
            break
        elif niche == ("warrior"):
            print ("You are now a warrior!")

            user_niche = ("warrior")
            break
        elif niche == ("inspect"):
            look_at_class()
