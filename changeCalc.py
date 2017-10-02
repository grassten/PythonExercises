# author: steven asten
# sloppy but it works
# project idea: https://www.reddit.com/r/beginnerprojects/comments/19jkn8/project_change_calculator/

billTotal = input("How much is the bill? ")
cashGiven = input("How much did the customer give? ")

change = cashGiven - billTotal

twenties = change / 20
change = change - (int(twenties) * 20)

tens = change / 10
change = change - (int(tens) * 10)

fives = change / 5
change = change - (int(fives) * 5)

ones = change / 1
change = change - int(ones)

quarters = change / .25
change = change - (int(quarters) * .25)

dimes = change / .1
change = change - (int(dimes) * .1)

nickels = change / .05
change = change - (int(nickels) * .05)

pennies = change / .01
change = change - (pennies * .01)

print("Bills: " + str(int(twenties)) + " twenties, " + str(int(tens)) + " tens, " + str(int(fives)) + " fives, and " + str(int(ones)) + " ones.")
print("Change: " + str(int(quarters)) + " quarters, " + str(int(dimes)) + " dimes, " + str(int(nickels)) + " nickels, and " + str(int(pennies)) + " pennies.")
