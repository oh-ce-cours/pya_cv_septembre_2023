def addition(a, b):
    return a.__add__(b) 

def test_un_truc():
    assert 1 == 1

def test_autre_chose():
    res = addition(3, 2)
    assert res == 5