count = 99


while count > 0:
    if count == 1:
        print(str(count) + " bottle of beer on the wall, " + str(count) + " bottle of beer...")
    else:
        print(str(count) + " bottles of beer on the wall, " + str(count) + " bottles of beer...")
    print
    count = count - 1
