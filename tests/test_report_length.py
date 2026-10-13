from lib.report_length import *

def test_report_length_when_five():
    response = report_length("flake")
    assert response == "This string was 5 characters long."