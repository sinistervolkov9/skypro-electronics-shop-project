from src.item import Item


class Keyboard(Item):

    def __init__(self, name: str, price: float, quantity: int, language: str = "EN"):
        super().__init__(name, price, quantity)
        self.__name = name
        self._language = language

        self._lang_list = ["EN", "RU"]

    @property
    def language(self):
        return self._language

    def change_lang(self):
        index = self._lang_list.index(self._language)
        if index == len(self._lang_list) - 1:
            self._language = self._lang_list[0]
        else:
            self._language = self._lang_list[index + 1]

    @language.setter
    def language(self, value):
        if value in self._lang_list:
            self._language = value
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
