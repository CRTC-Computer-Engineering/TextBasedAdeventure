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
        if input == (""):
            townsquare.ragni_square()
        else:
            townsquare.ragni_square()
    elif input == 2:
        print_detlas()
        ready = input("Ready to go to Detlas? Press ENTER when ready.")
        if input == (""):
            townsquare.detlas_square()
        else:
            townsquare.detlas_square()
    elif input == 3:
        print_almuj()
        ready = input("Ready to go to Almuj? Press ENTER when ready.")
        if input == (""):
            townsquare.almuj_square()
        else:
            townsquare.almuj_square()
    elif input == 4:
        print_nemract()
        ready = input("Ready to go to Nemract? Press ENTER when ready.")
        if input == (""):
            townsquare.nemract_square()
        else:
            townsquare.nemract_square()
    elif input == 5:
        print_nesaak()
        ready = input("Ready to go to Nesaak? Press ENTER when ready.")
        if input == (""):
            townsquare.nesaak_square()
        else:
            townsquare.nesaak_square()
    elif input == 6:
        print_troms()
        ready = input("Ready to go to Troms? Press ENTER when ready.")
        if input == (""):
            townsquare.troms_square()
        else:
            townsquare.troms_square()
    elif input == 7:
        print_rymek()
        ready = input("Ready to go to Rymek? Press ENTER when ready.")
        if input == (""):
            townsquare.rymek_sqaure()
        else:
            townsquare.rymek_sqaure()
    else:
        print ("That is not a valid option.")
        next_destination()

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
