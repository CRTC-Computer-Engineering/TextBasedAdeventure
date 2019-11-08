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
        self.attack = 17
        self.defence = 15
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
        print ("1. " + str(self.item1))
        print ("2. " + str(self.item2))
        print ("3. " + str(self.item3))
        print ("4. " + str(self.item4))
        print ("5. " + str(self.item5))
