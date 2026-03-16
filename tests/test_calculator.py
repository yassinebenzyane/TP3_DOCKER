import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.calculator import addition, multiplication


def test_addition():
    assert addition(2,3) == 5

def test_multiplication():
    assert multiplication(2,3) == 6