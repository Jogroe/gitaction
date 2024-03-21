import pytest
from moyenne import calculer_moyenne

def test_calculer_moyenne():
    assert calculer_moyenne([1, 2, 3, 4, 5]) == 3.0
    assert calculer_moyenne([]) == 0