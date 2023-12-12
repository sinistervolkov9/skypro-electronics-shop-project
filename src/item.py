import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = str(name)  # название товара
        self.price = price  # цена за единицу товара
        self.quantity = quantity  # количество товара в магазине
        self.all.append(self)  # Помещает товар в список обращаемых

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = float(self.price) * int(self.quantity)
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Одноименный с приватным атрибутом метод.
        Декоратор property берет метод, и позволяет к нему обращаться как к атрибуту
        """
        return self.__name

    @name.setter
    def name(self, name_str):
        """
        Сеттер
        """
        if len(str(name_str)) > 10:
            self.__name = str(name_str)[:10]
        else:
            self.__name = str(name_str)

    @classmethod
    def instantiate_from_csv(cls, path_str):
        with open(path_str, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if reader.fieldnames[0] == "name" and reader.fieldnames[1] == "price" and reader.fieldnames[2] == "quantity":
                for i in reader:
                    cls(i['name'], i['price'], i['quantity'])

    @staticmethod
    def string_to_number(string):
        return int(float(string))
