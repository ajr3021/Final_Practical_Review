from unit10_to_13 import *


def test_subset_true():
    set1 = {1, 2}
    set2 = {1, 2, 3}

    expected = True
    actual = subset(set1, set2)

    assert actual == expected

def test_subset_false():
    set1 = {1, 4}
    set2 = {1, 2, 3}

    expected = False
    actual = subset(set1, set2)

    assert actual == expected


def test_alphabetical_length():
    filename = 'alice.txt'

    result =  alphabetical_length(filename)

    assert result[10] == "yourself.'"
    assert result[3] == 'You'
    assert result[30] == "http://www.gutenberg.org/1/11/"


def test_validate_parethesis_true():
    string = "((1 + 3) / 4)"

    result = validate_parenthesis(string)
    assert result


def test_validate_parethesis_false():
    string = ")(15 * 91)"
    result = validate_parenthesis(string)
    assert not result


def test_validate_parethesis_no_parenthesis():
    string = "93 // 2"
    result = validate_parenthesis(string)
    assert result