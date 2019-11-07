#Used to print number of desired blank lines
def blank_line(lines):
    for i in range(lines):
        print ("")


#Used for inspecting classes inside of the class selection function
def look_at_class():
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
            user_object = ()
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
            user_object = Mage()
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
            inspect_class = input("What class would you like to inspect?")
            look_at_class()
