from hashmap_repeated_word.hashmap_repeated_word import first_repeated_word
import pytest
from hashtable.hashtable import Hashtable

def test_can_instantiate_a_hashamp():
    hashmap = Hashtable()
    assert hashmap


def test_empty_string_returns_None():
    input1 = ""
    actual = first_repeated_word(input1)
    assert actual == None


def test_no_repeats_returns_None():
    input1 = "aa bb cc ddd ee fff"
    actual = first_repeated_word(input1)
    assert actual == None


def test_will_return_first_repeated_word():
    input1 = "aa DDD aA cc ddd ee fff"
    actual = first_repeated_word(input1)
    assert actual == "aa"


def test_function_ignores_upper_and_lower_case():
    input1 = "aa DDD bb cc ddd ee fff"
    actual = first_repeated_word(input1)
    assert actual == "ddd"


def test_will_not_include_punctuations_in_check():
    input1 = "aa DDD bb cc ddd ee fff !DdD,"
    actual = first_repeated_word(input1)
    assert actual == "ddd"
