from unit1_to_5 import *


def test_alliteration_average():
    string = "writing alliterations was wack"
    result = alliteration(string)
    assert result


def test_alliteration_case():
    string = "Writing alliterations was wack"
    result = alliteration(string)
    assert result


def test_alliteration_false():
    string = "this is not an alliteration"
    result = alliteration(string)
    assert not result


def test_alliteration_50():
    string = "This was the hardest one TBH."
    result = alliteration(string)
    assert result


def test_pokemon_output_gen_1():
    expected = 147
    result = pokemon_output("pokemon.csv", 1)
    assert result == expected
    try:
        with open("output.txt") as out:
            assert True
    except FileNotFoundError:
        print("No file named output.txt was found")
        assert False


def test_pokemon_output_no_file():
    expected = 'FileNotFound'
    result = pokemon_output("fakefile.csv", 1)
    assert result == expected


def test_find_pokemon_name_143():
    excepted = 'Snorlax'
    result = find_pokemon_name("pokemon.csv", 143)
    assert excepted == result


def test_find_pokemon_name_no_file():
    expected = 'FileNotFound'
    result = pokemon_output("fakefile.csv", 1)
    assert result == expected

   