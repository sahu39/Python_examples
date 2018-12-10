#lambda demo 3#
def myfunc(n):
    return lambda x : x*n
def main():
    mydoubler = myfunc(2)
    mytripler = myfunc(3)
    print("Double value of 8 is :",mydoubler(8))
    print("Triple value of 8 is :",mytripler(8))


if __name__ == "__main__":
    main()
