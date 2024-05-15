#!/usr/bin/python3
"""
square
"""


class Square:
    """
    Represents a square shape.

    Attributes:
        width (int): The width of the square.
        height (int): The height of the square.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a square with the given width and height.

        Args:
            width (int): The width of the square. Default is 0.
            height (int): The height of the square. Default is 0.
        """
        self.width = width
        self.height = height

    def Area_of_my_square(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.width * self.width

    def Permiter_Of_My_Square(self):
        """
        Calculates the perimeter of the square.

        Returns:
            int: The perimeter of the square.
        """
        return self.width * 4

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: String representation of the square in the format:
            'width/height'.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.Area_of_my_square())
    print(s.Permiter_Of_My_Square())
