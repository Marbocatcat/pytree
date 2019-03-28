#!bin/env python3.7

import argparse
import pathlib
import os
from colorama import init, Fore, Back, Style

# autoreset=True clears the color.
init(autoreset=True)

# TODO: Add argparse description and help.
def parsed():
    # creates an argparse object.
    parser = argparse.ArgumentParser()
    # creates basic options and addes "target" as argument.
    parser.add_argument("target", nargs="?", default=pathlib.Path.cwd(), help="path to be examined.")
    # parse argument object.
    arg = parser.parse_args()

    return arg.target


def tree(dir):
    # create a pathlib object and assign to .
    dir = pathlib.Path(dir)
    print(f"{Fore.GREEN + str(dir)}\n     |")
    # grabs every path in the "dir" object that was created using pathlib and sorts them.
    for path in sorted(dir.rglob("*")):
        # dirparts" divides the rel path dir and takes the length of each one to be used in the spacer variable.
        depth = len(path.relative_to(dir).parts)
        spacer = "     |" * depth
        # return is red if path is a dir, else return is yellow.
        name = Fore.RED + path.name if path.is_dir() else Fore.YELLOW + path.name
        print(f"{spacer}`-- {name}")


def main():
    os.system("clear")
    # add "target" as argument.
    tree(parsed())


if __name__ == "__main__":
    main()
