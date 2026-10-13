import pytest
from lib.present import Present

#When we wrap an item we get it back when unwrapping
def test_present_wrap_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

#When we wrap an item and try to wrap again; error case 1
def test_present_wrap_when_already_wrapped():
    present = Present()
    present.wrap(33)
    with pytest.raises(Exception) as err:
        present.wrap(55)
    message = str(err.value)
    assert message == "A contents has already been wrapped."   

#Attempting to unwrap without first wrapping
def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    message = str(err.value)
    assert message == "No contents have been wrapped."
