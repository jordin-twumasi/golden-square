from lib.counter import Counter

def test_counter_when_single_number():
    counter = Counter()
    counter.add(5)
    assert counter.report()  == "Counted to 5 so far."

def test_counter_when_multiple_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    assert counter.report()  == "Counted to 8 so far."
