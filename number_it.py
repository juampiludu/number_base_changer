def number_it(myList, b, c):

    digits = []

    if b != 10:

        for i in myList:
            if i == "A" or i == "a":
                i = 10
            elif i == "B" or i == "b":
                i = 11
            elif i == "C" or i == "c":
                i = 12
            elif i == "D" or i == "d":
                i = 13
            elif i == "E" or i == "e":
                i = 14
            elif i == "F" or i == "f":
                i = 15
            elif i == "G" or i == "g":
                i = 16
            elif i == "H" or i == "h":
                i = 17
            elif i == "I" or i == "i":
                i = 18
            elif i == "J" or i == "j":
                i = 19
            elif i == "K" or i == "k":
                i = 20
            elif i == "L" or i == "l":
                i = 21
            elif i == "M" or i == "m":
                i = 22
            elif i == "N" or i == "n":
                i = 23
            elif i == "O" or i == "o":
                i = 24
            elif i == "P" or i == "p":
                i = 25
            elif i == "Q" or i == "q":
                i = 26
            elif i == "R" or i == "r":
                i = 27
            elif i == "S" or i == "s":
                i = 28
            elif i == "T" or i == "t":
                i = 29
            elif i == "U" or i == "u":
                i = 30
            elif i == "V" or i == "v":
                i = 31
            elif i == "W" or i == "w":
                i = 32
            elif i == "X" or i == "x":
                i = 33
            elif i == "Y" or i == "y":
                i = 34
            elif i == "Z" or i == "z":
                i = 35
            digits.append(int(i))
    
    
    if c != 10:

        for i in myList:
            if int(i) == 10:
                i = "A"
            elif int(i) == 11:
                i = "B"
            elif int(i) == 12:
                i = "C"
            elif int(i) == 13:
                i = "D"
            elif int(i) == 14:
                i = "E"
            elif int(i) == 15:
                i = "F"
            elif int(i) == 16:
                i = "G"
            elif int(i) == 17:
                i = "H"
            elif int(i) == 18:
                i = "I"
            elif int(i) == 19:
                i = "J"
            elif int(i) == 20:
                i = "K"
            elif int(i) == 21:
                i = "L"
            elif int(i) == 22:
                i = "M"
            elif int(i) == 23:
                i = "N"
            elif int(i) == 24:
                i = "O"
            elif int(i) == 25:
                i = "P"
            elif int(i) == 26:
                i = "Q"
            elif int(i) == 27:
                i = "R"
            elif int(i) == 28:
                i = "S"
            elif int(i) == 29:
                i = "T"
            elif int(i) == 30:
                i = "U"
            elif int(i) == 31:
                i = "V"
            elif int(i) == 32:
                i = "W"
            elif int(i) == 33:
                i = "X"
            elif int(i) == 34:
                i = "Y"
            elif int(i) == 35:
                i = "Z"
            digits.append(i)

    return digits