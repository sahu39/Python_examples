# setdefault() method #
def main():
    my_dict = {1:"Sunil","age":26,"Gender":"male"}
    val = my_dict.setdefault("Gender")
    print("list is:",my_dict,"val is:",val)
    print(my_dict.setdefault("place","berhampur"))
if __name__ == "__main__":
    main()
