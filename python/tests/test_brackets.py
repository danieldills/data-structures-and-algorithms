import pytest

from stack_queue_brackets.brackets import validate_brackets

def test_case_one():
    actual = validate_brackets("{}")
    expected = (True, "Balanced")
    assert actual == expected

def test_case_two():
    actual = validate_brackets("{}(){}")
    expected = (True, "Balanced")
    assert actual == expected

def test_case_three():
    actual = validate_brackets("()[[Extra Characters]]")
    expected = (True, "Balanced")
    assert actual == expected

def test_case_four():
    actual = validate_brackets("(){}[[]]")
    expected = (True, "Balanced")
    assert actual == expected

def test_case_five():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = (True, "Balanced")
    assert actual == expected

def test_case_six():
    actual = validate_brackets("[({}]")
    expected = (False, "Unbalanced")
    assert actual == expected

def test_case_seven():
    actual = validate_brackets("(](")
    expected = (False, "Unbalanced")
    assert actual == expected

def test_case_eight():
    actual = validate_brackets("{(})")
    expected = (False, "Unbalanced")
    assert actual == expected

def test_case_nine():
    actual = validate_brackets("")
    expected = (True, "Balanced")
    assert actual == expected

def test_case_ten():
    actual = validate_brackets("daniel")
    expected = (True, "Balanced")
    assert actual == expected
