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
        self.name = str(name)  # название товара
        self.price = price  # цена за единицу товара
        self.quantity = quantity  # количество товара в магазине
        self.all.append(self)  # Помещает товар в список обращаемых

    def calculate_total_price(self): # -> float
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        # Проверка, не являются ли аргументы цены или количества товара NoneType-объектами:
        if self.price is None or self.quantity is None:
            return "Value Error"
        else:
            # Проверка, не являются ли типы данных аргументов цены или количества товара недопустимыми:
            if type(self.price) not in [list, dict, set, bool]:
                if type(self.quantity) not in [list, dict, set, bool]:
                    # Проверка, можно ли преобразовать цену и количество товара в виде чисел:
                    try:
                        float(self.price)
                        float(self.quantity)
                        # Проверка, является ли количество товара целым чилсом
                        if float(self.quantity) % 2 != 0:
                            return "Value Error"
                        # Проверка, явлюяются ли аргументы цены или количества товара положительными числами:
                        elif float(self.price) < 0 or float(self.quantity) < 0:
                            return "Value Error"
                        else:
                            total_price = float(self.price) * int(self.quantity)
                            return total_price
                    except ValueError:
                        return "Value Error"
                else:
                    return "Value Error"
            else:
                return "Value Error"
    def apply_discount(self): # -> None
        """
        Применяет установленную скидку для конкретного товара.
        """
        # Проверка, не являются ли аргументы цены или коэфициент цены NoneType-объектами:
        if self.price is None:
            self.price = "Value Error"
        else:
            # Проверка, не являются ли типы данных аргументов цены или коэфициент цены недопустимыми:
            if type(self.price) not in [list, dict, set, bool]:
                if type(self.pay_rate) not in [list, dict, set, bool]:
                    # Проверка, можно ли преобразовать цену и коэфициент цены в виде чисел:
                    try:
                        float(self.price)
                        float(self.pay_rate)
                        # Проверка, явлюяются ли аргументы цены или коэфициент цены положительными числами:
                        if float(self.price) < 0:
                            self.price = "Value Error"
                        if self.pay_rate < 0:
                            self.price = "Value Error"
                        else:
                            self.price *= self.pay_rate
                    except:
                        self.price = "Value Error"
                else:
                    self.price = "Value Error"
            else:
                self.price = "Value Error"
