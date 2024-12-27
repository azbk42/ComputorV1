from computor import find_degres

def test_degres():
    assert find_degres("X^2 + X^1 = X^8") == 8, "result should be 8"
    assert find_degres("X + X^2") == 2, "result should be 2"
    assert find_degres ("2 = 2") == 0, "result should be 0"
    assert find_degres("X = 2") == 1, "result should be 1"
    assert find_degres("X") == 1, "result should be 1"
