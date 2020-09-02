import datetime
from buildings import *
from units import *
from constants import GOLD_COIN, MAX_GOLD_STORED


class Base(object):
    def __init__(self, buildings=[], garrison=[], generators=[], items=[]):
        self.buildings = buildings
        self.generators = generators
        self.garrison = garrison
        self.items = items
        self.gold = 0
        self.last_emptied = datetime.datetime.now()

    @property
    def gold(self):
        if len(self.generators) == 0:
            self._gold = 0
        else:
            self.gold = self.check_generators() % (MAX_GOLD_STORED * len(self.generators))
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = value

    @property
    def garrison(self):
        return self._garrison
    
    @garrison.setter
    def garrison(self, value):
        self._garrison = value
        
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, value):
        self._items = value

    @property
    def buildings(self):
        return self._buildings

    @buildings.setter
    def buildings(self, value):
        self._buildings = value

    @property
    def generators(self):
        return self._generators

    @generators.setter
    def generators(self, value):
        self._generators = value

    def build_generator(self):
        self.generators.append(Generator())

    def build_armory(self):
        self.buildings.append(Armory())

    def empty_generators(self):
        time_now = datetime.datetime.now()
        total_gold = self.check_generators(time_now)
        self.last_emptied = time_now
        return total_gold

    def check_generators(self, time_now=None):
        if time_now is None:
            time_now = datetime.datetime.now()
        minutes_passed = (time_now - self.last_emptied).seconds // 60
        total_gold = 0
        for generator in self.generators:
            total_gold += generator.empty(minutes_passed)
        return total_gold

    def hire_soldier(self):
        self.garrison.append(Man())

    def view_base(self):
        return self.__str__()

    def view_shop(self):
        shop_str = ""
        for building in self.buildings:
            shop_str += building.view_shop()
        return shop_str

    def buy_item(self, item_to_buy):
        item_list = {}
        for building in self.buildings:
            for item in building.items:
                item_list[item().name] = item
        if item_to_buy in item_list:
            item = item_list[item_to_buy]
            self.items.append(item())
            return True
        else:
            return False

    def __str__(self):
        generator_str = Generator().__str__() * len(self.generators)
        garrison_str = Man().__str__() * len(self.garrison)
        building_str = ""
        item_str = ""

        for building in self.buildings:
            building_str += str(building)
        for item in self.items:
            item_str += str(item)

        base_str = (
            "Buildings:\t{},\n"
            "Generators:\t{},\n"
            "Gold:\t{} {},\n"
            "Garrison:\t{},\n"
            "Items: {}"
        ).format(
            building_str,
            generator_str,
            self.gold,
            GOLD_COIN,
            garrison_str,
            item_str
        )
        return base_str
