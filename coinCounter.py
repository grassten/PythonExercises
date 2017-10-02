# author: Steven Asten
# practicing use of functions, user input, etc

def calculatePennies(pennyWeight):
    numPennies = weightPennies / 2.5
    print("    ..." + str(numPennies) + " pennies.")


def calculateNickels(nickelWeight):
    numNickels = weightNickels / 5.0
    print("    ..." + str(numNickels) + " nickels.")


def calculateDimes(dimeWeight):
    numDimes = weightDimes / 2.268
    print("    ..." + str(numDimes) + " dimes.")


def calculateQuarters(quarterWeight):
    numQuarters = weightQuarters / 5.67
    print("    ..." + str(numQuarters) + " quarters.")


def printYouHave():
    print("You have...")


weightPennies = input("Enter weight of pennies in grams: ")
weightNickels = input("Enter weight of nickels in grams: ")
weightDimes = input("Enter weight of dimes in grams: ")
weightQuarters = input("Enter weight of quarters in grams: ")

printYouHave()
calculatePennies(weightPennies)
calculateNickels(weightNickels)
calculateDimes(weightDimes)
calculateQuarters(weightQuarters)
