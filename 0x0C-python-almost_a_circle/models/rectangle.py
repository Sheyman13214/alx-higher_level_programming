#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle."""

    # class constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for width
    @property
    def width(self):
        """Get the width of thi Rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the Rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            ValueError: If value is not an integer or <= 0.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    # Getter and setter for height
    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the Rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            ValueError: If value is not an integer or <= 0.
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    # Getter and setter for x
    @property
    def x(self):
        """Get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """Set the x coordinate of the Rectangle.

        Args:
            value (int): The x coordinate value to be set.

        Raises:
            ValueError: If value is not an integer or < 0.
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    # Getter and setter for y
    @property
    def y(self):
        """Get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """Set the y coordinate of the Rectangle.

        Args:
            value (int): The y coordinate value to be set.

        Raises:
            ValueError: If value is not an integer or < 0.
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    # Rectangle Functionality
    def area(self):
        """Returns the area of the rectangle (int)"""
        return self.__height * self.__width

    def display(self):
        """
        Print the Rectangle instance using the character #.
        """
        if self.width == 0 or self.height == 0:
            print("")
            return
        print("\n"*self.y, end='')
        for line in range(self.__height):
            print(" "*self.x, end='')
            print('#'*self.__width)

    def update(self, *args, **kwargs):
        """
        Update attributes with provided arguments, positional and keyworded.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of Rectangle"""
        res = {
                'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width
                }
        return res

    # Built in functions
    def __str__(self):
        """
        Return a string representation of the Rectangle instance.
        """
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )
