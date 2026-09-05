from mathutils import add, subtract, is_even, is_prime


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(4) is False


def test_is_even():
    assert is_even(4) is True
    assert is_even(7) is False
