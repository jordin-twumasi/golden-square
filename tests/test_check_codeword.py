from lib.check_codeword import *

def test_check_codeword_is_horse():
    response = check_codeword('horse')
    assert response == "Correct! Come in."

def test_check_codeword_is_partly_right():
    response = check_codeword('hope')
    assert response == "Close, but nope."

def test_check_codeword_is_wrong():
    response = check_codeword('dog')
    assert response == "WRONG!"
