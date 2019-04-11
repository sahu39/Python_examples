#!/usr/bin/python3
#Reverse string using generator #
def main():
    def rev_str(x):
        length = len(x)
        for l in range(length-1,-1,-1):
            yield x[l] 

    for l in rev_str("hello"):
        print(l)

if __name__ == "__main__":
    main()

