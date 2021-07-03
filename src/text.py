from colorama import Fore

def success_msg(text):
    print(Fore.LIGHTGREEN_EX + text + Fore.WHITE)

def error_msg(text):
    print(Fore.LIGHTRED_EX + text + Fore.WHITE)

def warning_msg(text):
    print(Fore.YELLOW + text + Fore.WHITE)