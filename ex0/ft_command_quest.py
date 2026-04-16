#!/usr/bin/env python3
import sys


def main() -> None:
    print("=== Command Quest ===")

    args = sys.argv
    program_name = args[0]
    arguments = args[1:]

    print(f"Program name: {program_name}")

    if len(arguments) == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(arguments)}")
        for i in range(len(arguments)):
            print(f"Argument {i + 1}: {arguments[i]}")

    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
