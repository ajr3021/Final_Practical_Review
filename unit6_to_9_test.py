from unit6_to_9 import *
import io

def find_primes_test():
    limit = 10
    expexted = [2, 3, 5, 7]
    result = find_primes(limit)
    assert expexted == result


def test_letter_count_alice():
    filename = "alice.txt"
    expected = [9083, 1621, 2817, 5228, 15085, 2248, 2751, 7581, 7803, 222, 1202, 5053, 2245, 7871, 9244, 1796, 135, 6400, 6981, 11631, 3867, 911, 2696, 170, 2442, 79]
    actual = letter_count(filename)
    assert actual == expected


def test_letter_count_not_file():
    try:
        letter_count("fakefile.txt")
        assert True
    except FileNotFoundError:
        print("Exception no caught")
        assert False


def test_reverse_string():
    string = 'hello'
    expected = 'olleh'
    actual = reverse_string_recursive(string)
    assert expected == actual


def test_reverse_string_empty():
    string = ''
    exepected = ''
    actual = reverse_string_recursive(string)
    assert exepected == actual


def test_add(capsys, monkeypatch):
    pass
