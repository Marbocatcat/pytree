#!/bin/env python3.7
from colorama import Fore, Back, Style, init

init(autoreset=True)

print('This is normal.')
print(Fore.BLACK + Back.WHITE + 'This is reversed.')
print(Fore.WHITE + Back.RED + Style.BRIGHT + 'Alert!')
print(Fore.WHITE + Back.YELLOW + 'Alert!!')
