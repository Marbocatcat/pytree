#!bin/env python3.7

import argparse
import pathlib


def tree(directory):
    directory = pathlib.Path(directory) # create a pathlib object and assign to directory.
    print(f'{directory}\n      |')

    for path in sorted(directory.rglob("*")):   # grabs every path in the 'directory' object that was created using pathlib.
        depth = len(path.relative_to(directory).parts) # 'parts' divides the rel path directory and takes the length of each one.
        spacer = '      |' * depth

        print(f'{spacer}+-- {path.name}')

def main():
    parser = argparse.ArgumentParser()  # creates an argparse object.
    parser.add_argument("target", nargs="?", default=pathlib.Path.cwd())    # creates basic options and addes 'target' as argument.
    arg = parser.parse_args()   # parse argument object.

    tree(arg.target)    # add 'target' as argument.

if __name__ == '__main__':
    main()
