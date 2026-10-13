from lib.gratitudes import Gratitudes

#Test for outcome when empty list/ no items added
def test_gratitudes_for_empty_list():
    gratitude = Gratitudes()
    assert gratitude.format() == "Be grateful for: "
    
#Test for outcome when adding single item to list
def test_gratitudes_for_single_item():
    gratitude = Gratitudes()
    gratitude.add('life')
    assert gratitude.format() == "Be grateful for: life"

#Test for outcome when adding multiple items to list
def test_gratitudes_for_multiple_items():
    gratitude = Gratitudes()
    gratitude.add('life')
    gratitude.add('family')
    assert gratitude.format() == "Be grateful for: life, family"
