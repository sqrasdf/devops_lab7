from calculator import maximum, minimum, sum

def test_maximum():
    assert maximum([1,3,5]) == 5
    assert maximum([-10,-2,-1]) == -1

def test_minimum():
    assert minimum([1,4,7]) == 1
    assert minimum([-7,-4,-1]) == -7

def test_sum():
    assert sum([1,2,3]) == 6
    assert sum([-1,-2,-3]) == -6
    assert sum([1,10,100,1000]) == 1111