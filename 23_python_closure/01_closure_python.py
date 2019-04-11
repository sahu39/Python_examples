#!/usr/bin/python3
# pythpn closure example#
def main():
    def make_multiplier(n):
        def multiplier(x):
            return x*n
        return multiplier

    times3 = make_multiplier(3)
    times5 = make_multiplier(5)

    print(times3(9))
    print(times5(4))
    print(times5(times3(12)))


if __name__ == "__main__":
    main()

