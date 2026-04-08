import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from calculator import *
import pytest

def test_add():
    assert add(2,3)==5

def test_divide():
    assert divide(10,2)==5

def test_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(1,0)
