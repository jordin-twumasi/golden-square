from lib.string_builder import StringBuilder

def test_string_builder_outputs_empty_string():
    stringbuilder = StringBuilder()
    assert stringbuilder.output() == ""


def test_string_builder_outputs_single_string():
    stringbuilder = StringBuilder()
    stringbuilder.add('Dogs')
    assert stringbuilder.output() == 'Dogs'


def test_single_string_size():
    stringbuilder = StringBuilder()
    stringbuilder.add('Dogs')
    assert stringbuilder.size() == 4

def test_string_builder_outputs_multiple_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add('Dogs')
    stringbuilder.add(' ')
    stringbuilder.add('Cats')
    assert stringbuilder.output() == 'Dogs Cats'

def test_multiple_string_size():
    stringbuilder = StringBuilder()
    stringbuilder.add('Dogs')
    stringbuilder.add(' ')
    stringbuilder.add('Cats')
    assert stringbuilder.size() == 9
