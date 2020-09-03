from items import Sword
from constants import BASE_GENERATOR_GOLD
from component import Component


class Building(Component):
    def __init__(self, name, emoji_str):
        self.name = name
        self.emoji_str = emoji_str
        self.items = None

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    def view_shop(self):
        shoplist = "{}:\n".format(self.name)
        for item in self.items:
            shoplist += "\t{}\n".format(item().print())
        return shoplist


class Generator(Building):
    def __init__(self, name="generator", emoji_str=":cloud_lightning:"):
        self.name = name
        self.emoji_str = emoji_str
        self.gold = BASE_GENERATOR_GOLD

    def empty(self, minutes):
        return self.gold * minutes

    def __str__(self):
        return self.emoji_str


class Armory(Building):
    def __init__(self, name="armory", emoji_str=":shield:"):
        self.name = name
        self.emoji_str = emoji_str
        self.items = [Sword]

    def __str__(self):
        return self.emoji_str




BUILDINGS_SQL = {
    "generator": Generator,
    "armory": Armory
}