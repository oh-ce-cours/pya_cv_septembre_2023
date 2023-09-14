import fizz_buzz_retours_Nghiem

def test_fizz_buzz_3():
    res = fizz_buzz_retours_Nghiem.handle_number(3)
    assert res == "3 fizz"
    
def test_fizz_buzz_5():
    res = fizz_buzz_retours_Nghiem.handle_number(5)
    assert res == "5 buzz"

def test_fizz_buzz_15():
    res = fizz_buzz_retours_Nghiem.handle_number(15)
    assert res == "15 fizzbuzz"

def test_fizz_buzz_autre():
    res = fizz_buzz_retours_Nghiem.handle_number(4)
    assert res == "4"