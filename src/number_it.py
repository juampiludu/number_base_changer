from .has_letter import has_letter


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

    elif c != 10:

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
    "A": list(range(10, 37)),
    "B": list(range(11, 37)),
    "C": list(range(12, 37)),
    "D": list(range(13, 37)),
    "E": list(range(14, 37)),
    "F": list(range(15, 37)),
    "G": list(range(16, 37)),
    "H": list(range(17, 37)),
    "I": list(range(18, 37)),
    "J": list(range(19, 37)),
    "K": list(range(20, 37)),
    "L": list(range(21, 37)),
    "M": list(range(22, 37)),
    "N": list(range(23, 37)),
    "O": list(range(24, 37)),
    "P": list(range(25, 37)),
    "Q": list(range(26, 37)),
    "R": list(range(27, 37)),
    "S": list(range(28, 37)),
    "T": list(range(29, 37)),
    "U": list(range(30, 37)),
    "V": list(range(31, 37)),
    "W": list(range(32, 37)),
    "X": list(range(33, 37)),
    "Y": list(range(34, 37)),
    "Z": [36],
}


def check_letter(a, b):

    x = list(a)

    for i in x:

        if i in conditions.keys():

            if b in conditions[i]:
                return True
            else:
                return False


conditions_b = {
    2: list(range(2)),
    3: list(range(3)),
    4: list(range(4)),
    5: list(range(5)),
    6: list(range(6)),
    7: list(range(7)),
    8: list(range(8)),
    9: list(range(9)),
    10: list(range(10)),
}


def check_in_b(a, b):

    x = [str(a) for a in a]
    is_in_cond = None

    if b in conditions_b.keys() and has_letter(a) == False:

        for i in x:

            if int(i) not in conditions_b[b]:
                is_in_cond = False
            else:
                is_in_cond = True

    return is_in_cond
