#map demo 1#
def myfunc(n):
    return len(n)

def main():
    my_list = ["Hello","Hi","Bye"]
    x = map(myfunc,my_list)
    print("list is",my_list,"Length List is",list(x))

if __name__ == "__main__":
    main()
