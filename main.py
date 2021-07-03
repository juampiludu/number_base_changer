from src.base_changer import base_changer
from src.text import *
from src.operations import operate

print("Translate numbers between numeric systems.")
print("Ctrl-C to exit.")


def main():
    valid = True
    try:

        while valid:

            print("\n--------------------------------------\n")

            if user_operation() == 'single':
                single_number()
            else:
                multiple_operations()

    # Note: comment this section to display errors.
    # (*)
    except ValueError:
        error_msg(
            "Value Error: Number can only be alphanumeric. Bases can only be numeric. None field can be empty.\n"
        )
    # (*)

    except KeyboardInterrupt:
        print("\nGoodbye!")
        valid = False


# Future implementation
# def language():
#     print("Choose your language")
#     lang = input("[e]nglish / e[s]pañol? ")


def user_operation():
    print("What do you want to do?")
    choice = input("\nParse [s]ingle number or operate with [m]ultiple numbers? ")
    if choice == 's':
        return 'single'
    return 'multiple'


def single_number():
    num, from_base, to_base = (
        input("Number (n): "),
        int(input("From base (n)\u2095: ")),
        int(input("To base (n)\u2095\u2082: ")),
    )

    base_changer(num.upper(), from_base, to_base)

def multiple_operations():
    prefixes = ["+", "-", "*", "/"]
    op = input("What operation do you want to do [+, -, *, /]? ")
    valid = op.lower().startswith(tuple(prefixes))
    while valid:
        operate(op)
        break
    else:
        error_msg("Sorry, we don't recognize that command.")
        multiple_operations()


if __name__ == '__main__':
    main()