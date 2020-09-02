import math
from component import Component
from items import Sword


class Man(Component):
    def __init__(self, name="man"):
        self.damage = 20
        self.attack_speed = 1
        self.health = 100
        self.killed = False
        self.items = {}
        self.name = name

    def give_item(self, item):
        item_name = item.name
        if item_name not in self.items:
            self.damage += item.damage
            self.health += item.health
            self.items[item.body_part] = item
            return True
        else:
            return False

    def calculate_damage(self, time):
        damage = self.damage * int(math.floor(time))
        return damage

    def kill(self):
        self.health = 100
        self.killed = True

    def is_dead(self):
        return self.killed

    def is_alive(self):
        return not self.killed

    @property
    def health(self):
        item_health = 0
        for item in self.items:
            item_health += item.health
        return self._health + item_health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health cannot be less than 0")
        self._health = value

    def injure(self, damage):
        if damage > self.health:
            damage = self.health
        self.health -= damage

    @property
    def damage(self):
        item_damage = 0
        for item in self.items:
            item_damage += item.damage
        return self._damage + item_damage

    @damage.setter
    def damage(self, value):
        if value <= 0:
            raise ValueError("Damage cannot be less than or equal to 0")
        self._damage = value

    @property
    def attack_speed(self):
        return self._attack_speed

    @attack_speed.setter
    def attack_speed(self, value):
        if value <= 0:
            raise ValueError("Damage cannot be less than or equal to 0")
        self._attack_speed = value

    def __str__(self):
        return ":man_mage:"


def SwordsMan(Man):
    def __init__(self):
        Man.__init__("swordsman")
        self.give_item(Sword())


class Army(object):
    def __init__(self, units=[]):
        self.current_index = 0
        self._internal_list = [unit for unit in units]

    def next(self) -> Man:
        self.current_index += 1
        if self.current_index >= len(self._internal_list):
            self.current_index = 0
        return self._internal_list[self.current_index]

    def clear_dead(self):
        units_lost = 0
        for index, unit in enumerate(self._internal_list):
            if unit.is_dead():
                del self._internal_list[index]
                units_lost += 1
        return units_lost

    def men_remaining(self) -> Man:
        return any(unit.is_alive() for unit in self._internal_list)


UNITS_SQL = {
    "man": Man,
    "swordsman": SwordsMan,
}

