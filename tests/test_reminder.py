import pytest #needed for with to raise error
from lib.reminder import Reminder

def test_reminds_user_of_task():
    reminder = Reminder("Jordin")
    reminder.remind_me_to("Send the parcels")
    result = reminder.remind()
    assert result == "Send the parcels, Jordin!"


def test_raises_an_error_when_no_task():
    reminder = Reminder("Jordin")
    with pytest.raises(Exception) as err:
        reminder.remind()
    error_message = str(err.value)
    assert error_message == "No reminder set!"