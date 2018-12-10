# dictionary get() method  #
def main():
    my_dict = dict({1:"python",2:"C","language":"program"})
    print(my_dict.get("language"),my_dict["language"])
    print(my_dict.get("paisa"))

if __name__ == "__main__":
    main()
