import pytest
from lib.password_checker import PasswordChecker

#When password meets requirements
def test_password_checker_valid():
    passwordchecker = PasswordChecker()
    assert passwordchecker.check("Apple123") == True
    
def test_password_checker_invalid():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as err:
        passwordchecker.check("A123")
    message = str(err.value)
    assert message == "Invalid password, must be 8+ characters."