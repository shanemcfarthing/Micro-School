"""
A module containing unit tests for the 
simple functions in utils.py
"""

import pytest
from utils import add, divide, is_palindrome

def test_add():
    """Test that add() correctly sums two numbers."""
    assert add(2, 3) == 5

def test_divide():
    """Test that divide() returns correct quotient for non-zero denominator."""
    assert divide(10, 2) == 5

def test_divide_by_zero():
    """Test that divide() raises ValueError when dividing by zero."""
    with pytest.raises(ValueError):
        divide(10, 0)

def test_is_palindrome_true():
    """Test that is_palindrome() returns True for a palindrome string."""
    assert is_palindrome("racecar")

def test_is_palindrome_false():
    """Test that is_palindrome() returns False for a non-palindrome string."""
    assert not is_palindrome("hello")

@pytest.mark.parametrize("word", ["madam", "level", "radar"])
def test_is_palindrome_parametrized(word):
    """Parametrized test: checks multiple palindrome strings."""
    assert is_palindrome(word)
