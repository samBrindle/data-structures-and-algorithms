import pytest
from data_structures.hashtable import Hashtable

def test_exists():
    assert Hashtable

def test_null_key():
    pass

def test_contains():
    table = Hashtable()
    table.set('apple', 'banana')
    actual = table.contains('apple')
    expected = True
    assert actual == expected

def test_contains_multiple():
    table = Hashtable()
    table.set('apple', 'banana')
    table.set('attack', 'defend')
    actual = table.contains('attack')
    expected = True
    assert actual == expected


def test_keys():
    table = Hashtable()
    table.set('apple', 'banana')
    table.set('attack', 'defend')
    keys = table.keys()
    actual = keys
    expected = ['apple', 'attack']
    assert actual == expected



def test_get():
    table = Hashtable()
    table.set('apple', 'banana')
    actual = table.get('apple')
    expected = 'banana'
    assert actual == expected
