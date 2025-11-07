from src.bin_search import binary_search


def test_middle():
    assert binary_search([1, 2, 3, 4, 5], 4) == 3


def test_start():
    assert binary_search([1, 2, 3, 4], 2) == 1


def test_not_in_list():
    assert binary_search([1, 2, 3, 4], 5) == -1

def test_single_element():
    assert binary_search([5], 5) == 0


def test_single_element_not_found():
    assert binary_search([3], 5) == -1


def test_empty_array():
    assert binary_search([], 5) == -1


def test_end():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4


def test_beginning():
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
