from hello import add, subtract


def test_add():
    assert 3 == add(2, 1)

def test_subtract():
    assert 2 == subtract(3,1)
