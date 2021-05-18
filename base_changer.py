from has_letter import has_letter
from number_it import number_it, check_letter, check_in_b


def base_changer(a, b, c):

    check_a_b = check_letter(a, b)
    check_number = check_in_b(a, b)

    if check_number == False:
        print(
            "Error: The number you've entered contains a character that does not correspond to the chosen base."
        )
        return

    if check_a_b == False:
        print(
            "Error: There is a letter in the number you entered that does not correspond to the chosen base."
        )
        return

    if b <= 10 and has_letter(a) == True:
        print(
            "Error: Numbers which contain letters are only for bases higher or equal than 10.\n"
        )
        return

    if b < 2 or b > 36 or c < 2 or c > 36:
        print("Error: Bases can only be numbers between 2 and 36.\n")
        return

    # a is number
    # b is from_base
    # c is to_base

    # a_const is to always have the initial value of "a"
    a_const = a

    # If bases are equal, then the result is "a"
    if b == c:
        print(f"\nBases are equal, the result is: {a}")
        return

    # If from_base is different to 10, then it will
    # find the value of "a" at base 10 number
    if b != 10:
        print(f"\nProcess to obtain {a_const} on base 10:")

        # If from_base is higher than 10, then it will
        # replace all letters (if has) by numbers
        if b > 10:

            # hexas iterates "a" to build a list of its digits
            hexas = [str(a) for a in a]

            # digits will contain digits of "a" as a list.
            # iterate list hexas to extract its elements
            # and replace all letters by numbers
            digits = number_it(hexas, b, c)

        else:

            # If b is lower or equal to 10, then digits
            # only iterate "a"
            digits = [int(d) for d in str(a)]

        # dec_dis is a list of numbers product of a
        # formula that gives as result: digit * (from_base^counter)
        dec_dis = []

        # counter represent the length of digits, means, quantity of
        # digits number "a" has
        counter = len(digits)

        # this iterates digits and with formula given above,
        # append to dec_dis the resulting numbers.
        for i in digits:
            counter -= 1
            j = b ** counter
            k = i * j
            dec_dis.append(k)

            print(f"{i} x ({b}^{counter}) = {k}")

        # this finally sum all elements in list dec_dis
        # and return a number which is "a" in decimal system
        a = sum(dec_dis)

        k_str = [str(dec_dis) for dec_dis in dec_dis]
        print(f'\n= {" + ".join(k_str)}')

        print(f"\n{a_const} on base 10 = {a}")

    # If to_base is different to 10, then it will find the
    # value of "a" as a "c" or "to_base" number
    if c != 10:
        print(f"\nProcess to obtain number {a_const} on base {b} to base {c}:")

        # digits_c will contain digits of "a" as a list
        digits_c = []

        # formula to find number on base "c":
        # a = cq   r
        a = int(a)
        r = int(a % c)
        q = int((a - r) / c)

        digits_c.append(r)

        print(f"{a} = ({c} x {q}) + {r}")

        # formula will repeat steps until q = 0
        while q != 0:
            a = int(q)
            r = int(a % c)
            q = int((a - r) / c)

            digits_c.append(r)

            print(f"{a} = ({c} x {q}) + {r}")

        # the digits of the new number are all the "r" of
        # formulas above, so we need to reverse digits_c list
        digits_c.reverse()

        # digits_c_str transforms to string all elements of
        # digits_c
        digits_c_str = [str(digits_c) for digits_c in digits_c]

        # new_hexas will contain numbers and letters.
        # this iterates digits_c_str to replace numbers by letters
        new_hexas = number_it(digits_c_str, b, c)
        new_hexas_str = [str(new_hexas) for new_hexas in new_hexas]

        # "a" take new value, that is the result of
        # joining all element of new_hexas to one string
        a = "".join(new_hexas_str)

        print(f"\n{a_const} on base {c} = {a}")

    if c > 10:
        print(
            "Note: remember to replace numbers with respective letters on bases higher than 10.\n"
        )
