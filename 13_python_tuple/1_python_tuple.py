#Basic tuple #
def main():
    thistuple = (1,2,3,"Hello")
    print(thistuple)
    #nested tuple
    tuple1=1,2,4,(3,"rr","jai")
    print(tuple1)
    #Tupel unpacking
    a,b,c,d = tuple1
    print(a,b,c,d)

if __name__ == "__main__":
    main()
