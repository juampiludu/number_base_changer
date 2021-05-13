def number_it(myList, b, c):

    digits = []

    if b != 10:

        for i in myList:
            if i == "A":
                i = 10
            elif i == "B":
                i = 11
            elif i == "C":
                i = 12
            elif i == "D":
                i = 13
            elif i == "E":
                i = 14
            elif i == "F":
                i = 15
            elif i == "G":
                i = 16
            elif i == "H":
                i = 17
            elif i == "I":
                i = 18
            elif i == "J":
                i = 19
            elif i == "K":
                i = 20
            elif i == "L":
                i = 21
            elif i == "M":
                i = 22
            elif i == "N":
                i = 23
            elif i == "O":
                i = 24
            elif i == "P":
                i = 25
            elif i == "Q":
                i = 26
            elif i == "R":
                i = 27
            elif i == "S":
                i = 28
            elif i == "T":
                i = 29
            elif i == "U":
                i = 30
            elif i == "V":
                i = 31
            elif i == "W":
                i = 32
            elif i == "X":
                i = 33
            elif i == "Y":
                i = 34
            elif i == "Z":
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


conditions = {
    'A': list(range(10,36)),
    'B': list(range(11,36)),
    'C': list(range(12,36)),
    'D': list(range(13,36)),
    'E': list(range(14,36)),
    'F': list(range(15,36)),
    'G': list(range(16,36)),
    'H': list(range(17,36)),
    'I': list(range(18,36)),
    'J': list(range(19,36)),
    'K': list(range(20,36)),
    'L': list(range(21,36)),
    'M': list(range(22,36)),
    'N': list(range(23,36)),
    'O': list(range(24,36)),
    'P': list(range(25,36)),
    'Q': list(range(26,36)),
    'R': list(range(27,36)),
    'S': list(range(28,36)),
    'T': list(range(29,36)),
    'U': list(range(30,36)),
    'V': list(range(31,36)),
    'W': list(range(32,36)),
    'X': list(range(33,36)),
    'Y': list(range(34,36)),
    'Z': [35],
}


def check_letter(a, b):

    x = list(a)

    for i in x:

        if i in conditions.keys():

            if b in conditions[i]:
                return True
            else:
                return False