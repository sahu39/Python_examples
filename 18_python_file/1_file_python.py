#!/usr/bin/python3
#File basic examples #

def main():
    with open("test.txt", mode = 'w', encoding = 'utf-8') as f:
        f.write("My 1st file & operation on python\n")
        f.write("This file contains\n")
        f.write("three lines\n")


if __name__ == "__main__":
    main()

