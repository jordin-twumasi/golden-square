from lib.greet import *
def test_greet_when_name_is_Jo():
    response = greet("Jo")
    assert response == "Hello, Jo!"