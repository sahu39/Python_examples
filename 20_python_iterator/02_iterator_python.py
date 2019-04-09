#!/usr/bin/python3
# PowTwo class using iterator#
def main():
    class PowTwo:
        def __init__(self,max = 0):
            self.max = max

        def __iter__(self):
            self.n = 0
            return self

        def __next__(self):
            if self.n <= self.max:
                result = 2 ** self.n
                self.n += 1
                return result

            else:
                raise StopIteration
    
    my_obj = PowTwo(4)
    iter_obj = iter(my_obj)
    print(next(iter_obj))
    print(next(iter_obj))
    print(next(iter_obj))
    print(next(iter_obj))
    print(next(iter_obj))
   # print(next(iter_obj))

if __name__ == "__main__":
    main()

