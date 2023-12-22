from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__name = name
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.__name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if int(value) < 1 or not isinstance(value, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self._number_of_sim = value

    # def check_sim(self):
    #     if int(self._number_of_sim) < 1 or not isinstance(self._number_of_sim, int):
    #         return "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."
    #     else:
    #         return None
