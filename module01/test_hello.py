'''from hello import add

def test_add():
    assert 2 == add(1, 1)'''

from hello import find_hash_with_two_leading_zeros

def test_hello():
    assert find_hash_with_two_leading_zeros(10000) is True