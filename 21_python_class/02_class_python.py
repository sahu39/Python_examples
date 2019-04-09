#!/usr/bin/python3
#python class example #
def main():
    class Rectangle:
        def __init__(self,length,breadth,unit_cost = 0):
            self.length = length
            self.breadth = breadth
            self.unit_cost = unit_cost

        def get_perimeter(self):
            return 2*(self.length+self.breadth)

        def get_area(self):
            return (self.length*self.breadth)

        def get_cost(self):
            area = self.get_area()
            return (area * self.unit_cost)

    r =  Rectangle(120,160,1000)
    print("Area of Reactangle is %s cm^2",str(r.get_area()))
    print("Unit cost %s Rs/-",str(r.get_cost()))


if __name__ == "__main__":
    main()

