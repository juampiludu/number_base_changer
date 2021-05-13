import re

def has_letter(string):
    return bool(re.search(r'\D', string))