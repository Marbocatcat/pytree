#!bin/env python3.7

import argparse
import pathlib
import os
from colorama import init, Fore, Back, Style

init(autoreset=True) # autoreset=True clears the color.

# TODO: Add argparse description and help.
# TODO: Consise way to write the code.

def tree(directory):
    directory = pathlib.Path(directory) # create a pathlib object and assign to directory.
    print(f'{Fore.GREEN + str(directory)}\n     |')

    for path in sorted(directory.rglob("*")):   # grabs every path in the 'directory' object that was created using pathlib and sorts them.
        depth = len(path.relative_to(directory).parts) # 'parts' divides the rel path directory and takes the length of each one to be used in the spacer variable.
        spacer = '     |' * depth

        if path.is_dir():   # if path is a directory color RED.
            name = Fore.RED + path.name
        else:               # if path is a file color YELLOW.
            name = Fore.YELLOW + path.name

        print(f'{spacer}`-- {name}')


def main():
    parser = argparse.ArgumentParser()  # creates an argparse object.
    parser.add_argument("target", nargs="?", default=pathlib.Path.cwd())    # creates basic options and addes 'target' as argument.
    arg = parser.parse_args()   # parse argument object.

    os.system('clear')
    tree(arg.target)    # add 'target' as argument.


if __name__ == '__main__':
    main()
