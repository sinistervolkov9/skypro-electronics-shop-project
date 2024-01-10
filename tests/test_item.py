from src.item import Item
import pytest


def test_calculate_total_price():
    item_1 = Item("Смартфон", 10000, 10)
    item_2 = Item("Смартфон", 10000, 0)
    item_3 = Item("Смартфон", 0, 10)
    item_4 = Item("Смартфон", 0, 0)

    #

    assert item_1.calculate_total_price() == 100000
    assert item_2.calculate_total_price() == 0
    assert item_3.calculate_total_price() == 0
    assert item_4.calculate_total_price() == 0


def test_apply_discount():
    Item.pay_rate = 1.0
    item_1 = Item("Смартфон", 10000, 10)
    item_1.apply_discount()

    Item.pay_rate = 2.0
    item_2 = Item("Смартфон", 10000, 10)
    item_2.apply_discount()

    #

    assert item_1.price == 10000
    assert item_2.price == 20000


def test_property():
    item = Item("Смартфон", 10000, 10)
    # длина наименования товара меньше 10 символов
    item.name = 'Флешка'
    assert item.name == 'Флешка'

    # длина наименования товара больше 10 символов
    item.name = 'Фотоаппарат'
    assert item.name == 'Фотоаппара'


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv('items.csv')

    #

    assert len(Item.all) == 5

def test_instantiate_from_csv_error():
    Item.instantiate_from_csv()

    #

    assert FileNotFoundError("отсутствует файл items.csv")

def test_string_to_number():
    item1 = Item.all[0]

    #

    assert item1.name == 'Смартфон'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr_n_str():
    item1 = Item("Смартфон", 10000, 20)

    #

    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_add():
    item_1 = Item("Смартфон", 10000, 10)
    item_2 = Item("Смартфон", 10000, 20)

    #

    assert item_1 + item_2 == 30


if __name__ == "__main__":
    test_calculate_total_price()
    test_apply_discount()
    test_property()
    test_instantiate_from_csv()
    test_instantiate_from_csv_error()
    test_repr_n_str()
    test_add()
    #   print("Всё ок!")
