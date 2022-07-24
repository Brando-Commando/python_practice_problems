from doctest import OutputChecker
from operator import truediv
import leap_year

def test_one():

    output = leap_year.is_leap(2000)
    assert output == True

def test_two():

    output = leap_year.is_leap(2100)
    assert output == False

def test_three():

    output = leap_year.is_leap(2400)
    assert output == True

def test_four():

    output = leap_year.is_leap(3455)
    assert output == False

def test_five():

    output = leap_year.is_leap(1992)
    assert output == True
