from base_changer import base_changer
from has_letter import has_letter
import sys

print("Translate numbers between numeric systems.")
print("Ctrl-C to exit.\n")

valid = True

while valid:

    try:

        num, from_base, to_base = (
            input("Number (n): "),
            int(input("From base (n)\u2095: ")),
            int(input("To base (n)\u2095\u2082: ")),
        )

        base_changer(num, from_base, to_base)

    except ValueError:
        if from_base < 10 and has_letter(num) == True:
            print("Numbers with letters are only for bases higher or equal than 10.")
        else:
            print("Bases must be integers between 2 and 16.")

    except KeyboardInterrupt:
        print("\nGoodbye!")
        valid = False