#!/usr/bin/python3
""" square class """


class Square:
    """square class"""

    def __init__(self, width=0):
        """ init the class"""
        self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width 

    def permiter_of_my_square(self):
        """ Perimeter of the square """
        return self.width * 4

    def __str__(self):
        """ str """
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":

    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
