from src.checksum import modulo11_checksum


def test_good():
    assert modulo11_checksum("2-266-11156-8")


def test_bad():
    assert not modulo11_checksum("2-266-11156-3")

def test_good_simple():
    assert modulo11_checksum("0306406152")


def test_bad_simple():
    assert not modulo11_checksum("0306406153")


def test_short():
    assert not modulo11_checksum("123")


def test_empty():
    assert not modulo11_checksum("")


def test_with_spaces():
    assert modulo11_checksum("0 306 40615 2")


def test_with_x():
    assert modulo11_checksum("012000030X")
