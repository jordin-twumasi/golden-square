#Need to import function we want to test
from lib.add_five import * 

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8 #assert to test if right value returned