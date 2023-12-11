from src.item import Item


def test_calculate_total_price():
    item_1 = Item("Смартфон", 10000, 10)
    item_2 = Item("Смартфон", "10000", 10)
    item_3 = Item("Смартфон", "10000", "10")

    item_4 = Item(10000, "abc", "qwe")

    item_5 = Item("Смартфон", 10000, 10.5)

    item_6 = Item(None, 10000, 10.5)
    item_7 = Item(None, None, 10.5)
    item_8 = Item(None, None, None)

    # item_9 = Item(["Смартфон"], 10000, 10)
    item_10 = Item(["Смартфон"], {10000}, 10)
    item_11 = Item(["Смартфон"], [10000], {10})
    item_12 = Item("Смартфон", True, 10)
    item_13 = Item("Смартфон", 10000, False)

    item_14 = Item("Смартфон", 10000, 0)
    item_15 = Item("Смартфон", 0, 10)
    item_16 = Item("Смартфон", 0, 0)

    item_17 = Item("Смартфон", 10000, -10)
    item_18 = Item("Смартфон", -10000, 10)
    item_19 = Item("Смартфон", 10000, "-10")
    item_20 = Item("Смартфон", "-10000", 10)

    #

    assert item_1.calculate_total_price() == 100000
    assert item_2.calculate_total_price() == 100000
    assert item_3.calculate_total_price() == 100000
    assert item_4.calculate_total_price() == "Value Error"
    assert item_5.calculate_total_price() == "Value Error"
    assert item_6.calculate_total_price() == "Value Error"
    assert item_7.calculate_total_price() == "Value Error"
    assert item_8.calculate_total_price() == "Value Error"
    # assert item_9.calculate_total_price() == 100000
    assert item_10.calculate_total_price() == "Value Error"
    assert item_11.calculate_total_price() == "Value Error"
    assert item_12.calculate_total_price() == "Value Error"
    assert item_13.calculate_total_price() == "Value Error"
    assert item_14.calculate_total_price() == 0
    assert item_15.calculate_total_price() == 0
    assert item_16.calculate_total_price() == 0
    assert item_17.calculate_total_price() == "Value Error"
    assert item_18.calculate_total_price() == "Value Error"
    assert item_19.calculate_total_price() == "Value Error"
    assert item_20.calculate_total_price() == "Value Error"


def test_apply_discount():
    Item.pay_rate = 1.0
    item_1 = Item("Смартфон", 10000, 10)
    item_1.apply_discount()

    Item.pay_rate = -1.0
    item_2 = Item("Смартфон", 10000, 10)
    item_2.apply_discount()

    Item.pay_rate = -1.7
    item_3 = Item("Смартфон", 10000, 10)
    item_3.apply_discount()

    Item.pay_rate = 1.0
    item_4 = Item("Смартфон", -10000, 10)
    item_4.apply_discount()


    Item.pay_rate = 2.0
    item_5 = Item("Смартфон", 10000, 10)
    item_5.apply_discount()

    #

    assert item_1.price == 10000
    assert item_2.price == "Value Error"
    assert item_3.price == "Value Error"
    assert item_4.price == "Value Error"
    assert item_5.price == 20000

if __name__ == "__main__":
    test_calculate_total_price()
    test_apply_discount()
    # print("Всё ок!")
