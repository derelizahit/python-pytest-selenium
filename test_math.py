import pytest

def add_two_numbers(a, b):
    return a + b

@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(1, 2) == 3, "ERROR: one plus two equals three"

@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(1020, 1040) == 2060, "ERROR: it should be 2060"
