from src.keyboard import Keyboard


def test_dunder_methods():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    #

    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_change_lang():
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    assert str(kb.language) == "EN"

    kb.language = 'CH'
    # AttributeError: property 'language' of 'Keyboard' object has no setter


if __name__ == "__main__":
    test_dunder_methods()
    test_change_lang()
