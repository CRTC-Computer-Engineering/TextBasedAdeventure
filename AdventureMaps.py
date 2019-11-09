#This file contains all the maps that can be called whilst traveling


def new_destination():
    print ("You are currently in " + city + ".")
    if city == ("Ragni"):
        print_ragni()
    elif city == ("Detlas"):
        print_detlas()
    elif city == ("Almuj"):
        print_almuj()
    elif city == ("Nemract"):
        print_nemract()
    elif city == ("Nesaak"):
        print_nesaak()
    elif city == ("Troms"):
        print_troms()
    elif city == ("Rymek"):
        print_rymek()
    else:
        print ("Something went totally wrong!")

def next_destination():
    print ("""---------------------------------------------
1. Ragni
2. Detlas
3. Almuj
4. Nemract
5. Nesaak
6. Troms
7. Rymek
---------------------------------------------""")
    input = int(input("Where would you like to go next?" ))
    if input == 1:
        print_ragni()
        ready = input("Ready to go to Ragni? Press ENTER when ready.")
        if input = (""):
            townsquare.ragni_square()
        else:
            townsquare.ragni_square()


def print_ragni():
    print ("")

def print_detlas():
    print ("")

def print_almuj():
    print ("")

def print_nemract():
    print ("")

def print_nesaak():
    print ("")

def print_troms():
    print ("")

def print_rymek():
    print ("")
