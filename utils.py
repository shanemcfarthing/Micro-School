"""
A module containing some simple functions.
"""

def add(a, b):
    """
    Return the sum of two numbers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def divide(a, b):
    """
    Divide a by b.

    Args:
        a (int or float): Numerator.
        b (int or float): Denominator.

    Raises:
        ValueError: If b is zero.

    Returns:
        float: The result of a divided by b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def multiply(a, b):
    """
    Return the product of two numbers.

    Args:
        a (int or float): First number.
        b (int or float): Second number.

    Returns:
        int or float: The product of a and b.
    """
    return a * b

def is_palindrome(s):
    """
    Check if a string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if s is a palindrome, False otherwise.
    """
    return s == s[::-1]
