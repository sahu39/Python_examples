#!/usr/bin/python3
#python generator example #
def main():
    def mygen():
        n = 1
        print('This is printed first')
        yield n

        n += 1
        print('This is printed  2nd')
        yield n

        n += 1
        print('This is printed last')

    a = mygen()
    print(next(a))
    print(next(a))
    print(next(a))


if __name__ == "__main__":
    main()

