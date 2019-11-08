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
