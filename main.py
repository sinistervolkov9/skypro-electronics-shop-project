from src.item import Item

if __name__ == '__main__':
    # item1 = Item("Смартфон", 10000, 20)
    # item2 = Item("Ноутбук", 20000, 5)
    #
    # print(item1.calculate_total_price())  # 200000
    # print(item2.calculate_total_price())  # 100000
    #
    # # устанавливаем новый уровень цен
    # Item.pay_rate = 0.8
    # # применяем скидку
    # item1.apply_discount()
    #
    # print(item1.price)  # 8000.0
    # print(item2.price)  # 20000
    #
    # print(Item.all)  # [<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]

    # дз2

    # item = Item('Телефон', 10000, 5)
    #
    # # длина наименования товара меньше 10 символов
    # item.name = 'Смартфон'
    #
    # # длина наименования товара больше 10 символов
    # item.name = 'СуперСмартфон'
    # # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла

    # item1 = Item.all[0]
    # assert item1.name == 'Смартфон'
    # assert Item.string_to_number('5') == 5
    # assert Item.string_to_number('5.0') == 5
    # assert Item.string_to_number('5.5') == 5

    # дз3

    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
