import pytest
from code_challenges.quick_sort import quick_sort

def test_full_list():
    list = [16, 8, 12, 4, 2]
    actual = quick_sort(list)
    expected = [2, 4, 8, 12, 16]

    assert actual == expected
