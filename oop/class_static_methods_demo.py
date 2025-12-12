"""
This module demonstrates the differences between class methods and static methods
"""


class Calculator:
    """A calculator class demonstrating static and class methods."""
    
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Add two numbers together.
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Multiply two numbers together.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
