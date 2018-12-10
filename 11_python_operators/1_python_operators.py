# Identity Operator #
def main():
    x=["apple","banana"]
    y=["apple","banana"]
    z=x
    print("x is y:"+ str(x is y))
    print("x is not y:"+ str(x is not y))

if __name__ == "__main__":
    main()
