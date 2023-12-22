from src.item import Item
from src.phone import Phone


def test_dunder_methods():
    phone_1 = Phone("iPhone 14", 120_000, 5, 2)
    phone_2 = Phone("iPhone 11", 60_000, 10, 2)

    #

    assert str(phone_1) == 'iPhone 14'
    assert repr(phone_1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone_1.number_of_sim == 2
    assert phone_1 + phone_2 == 15


def test_add():
    phone_1 = Phone("iPhone 14", 120_000, 5, 2)
    item_1 = Item("Смартфон", 10000, 20)

    #

    assert item_1 + phone_1 == 25


def test_check_sim():
    phone_1 = Phone("iPhone 14", 120_000, 5, 0)
    phone_2 = Phone("iPhone 14", 120_000, 5, 2.5)
    phone_3 = Phone("iPhone 14", 120_000, 5, 2)

    #

    # assert phone_1.check_sim() == "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."
    # assert phone_2.check_sim() == "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."
    # assert phone_3.check_sim() is None


if __name__ == "__main__":
    test_dunder_methods()
    test_add()
    test_check_sim()
