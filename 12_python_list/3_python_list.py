# List append() method #
# List remove() method #
def main():
    thelist = ["apple","mango","banana"]
    print("Before append:"+str( thelist))
    thelist.append("orange")
    print("After append:"+str(thelist))
    thelist.remove("mango")
    print("After remove"+str(thelist))

if __name__ == "__main__":
    main()
