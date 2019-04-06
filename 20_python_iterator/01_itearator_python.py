#!/usr/bin/python3
#python iterator #
def main():
    my_list = [1,2,3,4]
    my_iter = iter(my_list)

    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))


if __name__ == "__main__":
    main()

