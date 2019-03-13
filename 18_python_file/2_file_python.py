#!/usr/bin/python3
#File basic write and read examples #

def main():
    with open("test.txt", mode = "r+", encoding = 'utf-8') as f:
        f.write("My 1st file & operation on python\n")
        f.write("This file contains\n")
        f.write("three lines\n")
        for line in f:
            print(line, end = '')



if __name__ == "__main__":
    main()

