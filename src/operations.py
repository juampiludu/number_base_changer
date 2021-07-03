import operator
from .base_changer import base_changer
from .text import *

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv
}

def operate(op):

    warning_msg("\nEnter the first number:")
    num, from_base = (
        input("Number (n): "),
        int(input("From base (n)\u2095: ")),
    )
    num_const = num
    num = base_changer(num.upper(), from_base, 10)

    warning_msg("\nEnter the second number:") 
    num2, from_base2 = (
        input("Number (n): "),
        int(input("From base (n)\u2095: ")),
    )
    num_const2 = num2
    num2 = base_changer(num2.upper(), from_base2, 10)

    new_num = ops[op](int(num), int(num2))

    to_base = int(input("To base (n)\u2095\u2082: "))

    result = base_changer(str(new_num), 10, to_base)

    success_msg(f'\n({num_const}) on base {from_base} {op} ({num_const2}) on base {from_base2} = ({result}) on base {to_base}')