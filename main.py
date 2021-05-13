from base_changer import base_changer
import sys

print("Translate numbers between numeric systems.")
print("Ctrl-C to exit.")

valid = True

while valid:

    try:

        num, from_base, to_base = (
            input("\nNumber (n): "),
            int(input("From base (n)\u2095: ")),
            int(input("To base (n)\u2095\u2082: ")),
        )

        base_changer(num.upper(), from_base, to_base)

    except ValueError:
        print("Value Error: Bases can only be numeric.\n")

    except KeyboardInterrupt:
        print("\nGoodbye!")
        valid = False