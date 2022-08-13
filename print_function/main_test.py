from __future__ import print_function
import main
import sys

def test_one(capfd):

    print_function("5")
    # output = main.print_function(5)

    out, err = capfd.readouterr()
    assert out == "12345"

    # assert output == "12345"