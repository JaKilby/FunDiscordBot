from constants import GOLD_COIN, SWORD_COST, SHIELD_COST
from component import Component


class Item(Component):
    def __init__(self, name, price, damage, health, emoji_str, hand):
        self.name = name
        self.price = price
        self.damage = damage
        self.health = health
        self.emoji_str = emoji_str
        self.body_part = hand

    def print(self):
        return "{} {}: {} {}".format(self.name, str(self), self.price, GOLD_COIN)

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        if value < 0:
            raise ValueError("Item damage cannot be less than 0")
        self._damage = value

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Item health cannot be less than 0")
        self._health = value

    @property
    def body_part(self):
        return self._body_part

    @body_part.setter
    def body_part(self, value):
        if not value:
            raise ValueError(("Hand needs to be one of [\"chest\", \"head\", "
                              "\"legs\", \"feet\", \"right_hand\", \"left_hand\")"))
        self._body_part = value


class Sword(Item):
    def __init__(self, name="sword", price=SWORD_COST, damage=10, health=0, emoji_str=":crossed_swords:"):
        self.name = name
        self.price = price
        self.damage = damage
        self.health = health
        self.emoji_str = emoji_str
        self.body_part = "right_hand"

    def __str__(self):
        return self.emoji_str


class Sword(Item):
    def __init__(self, name="sword", price=SHIELD_COST, damage=0, health=30, emoji_str=":shield:"):
        self.name = name
        self.price = price
        self.damage = damage
        self.health = health
        self.emoji_str = emoji_str
        self.body_part = "right_hand"

    def __str__(self):
        return self.emoji_str


ITEMS_SQL = {
    "sword": Sword
}
