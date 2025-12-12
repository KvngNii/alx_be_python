"""
Polymorphism Demo - Demonstrating method overriding in Python
"""

import math


class Shape:
    """Base class for geometric shapes."""
    
    def area(self):
        """
        Calculate the area of the shape.
        
        Raises:
            NotImplementedError: Derived classes must override this method.
        """
        raise NotImplementedError("Derived classes must override the area() method")


class Rectangle(Shape):
    """Rectangle shape class that inherits from Shape."""
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle with length and width.
        
        Args:
            length: The length of the rectangle.
            width: The width of the rectangle.
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            The area calculated as length × width.
        """
        return self.length * self.width


class Circle(Shape):
    """Circle shape class that inherits from Shape."""
    
    def __init__(self, radius):
        """
        Initialize a Circle with a radius.
        
        Args:
            radius: The radius of the circle.
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            The area calculated as π × radius².
        """
        return math.pi * self.radius ** 2
