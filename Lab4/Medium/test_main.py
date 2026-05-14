from main import (
    to_str_recursive,
    to_str_iterative,
    a_recursive,
    a_iterative
)

def test_to_str_recursive():
    x = [1, [2, [3, [4, [5]]]]]
    expected = "1 -> 2 -> 3 -> 4 -> 5 -> None"

    assert to_str_recursive(x) == expected

def test_to_str_iterative():
    x = [1, [2, [3, [4, [5]]]]]
    expected = "1 -> 2 -> 3 -> 4 -> 5 -> None"

    assert to_str_iterative(x) == expected

def test_a_recursive():
    assert round(a_recursive(5), 10) == round(1.4794921875, 10)

def test_a_iterative():
    assert round(a_iterative(5), 10) == round(1.4794921875, 10)
