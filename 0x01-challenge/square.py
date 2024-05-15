#!/usr/bin/python3
""" square class """


class Square:
    """square class"""

    def __init__(self, width=0, height=0):
        """ init the class"""
        self.width = width
        self.height = height

    def Area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width 

    def Permiter_Of_My_Square(self):
        """ Perimeter of the square """
        return self.width * 4

    def __str__(self):
        """ str """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.Area_of_my_square())
    print(s.Permiter_Of_My_Square())
