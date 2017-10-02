# author: steven asten
# find order total
# idea from https://www.reddit.com/r/beginnerprojects/comments/1bytu5/projectmenu_calculator/

print("1. Chicken Strips - $3.50")
print("2. French Fries - $2.50")
print("3. Hamburger - $4.00")
print("4. Hotdog - $3.50")
print("5. Drink - $1.75")

order = input("Input order by IDs: ")

i = 0
total = 0

while i < len(str(order)):
    if str(order)[i] == str(1):
        total = total + 3.5
    elif str(order)[i] == str(2):
        total = total + 2.5
    elif str(order)[i] == str(3):
        total = total + 4
    elif str(order)[i] == str(4):
        total = total + 3.5
    elif str(order)[i] == str(5):
        total = total + 1.75

    i = i + 1

print("Total: $%.2f" % total)
