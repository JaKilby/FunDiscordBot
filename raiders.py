import psycopg2 as sql
import os
import math
from units import Man, Army
from buildings import Generator
from constants import GOLD_COIN, GENERATOR_COST, SOLDIER_COST, ARMORY_COST, ITEM_PRICE_MAP
from base import Base, BUILDINGS_SQL
from items import ITEMS_SQL
from units import UNITS_SQL
import sys

ADMIN_LIST = [199256185201885184]

class RaidersManager(object):
    def __init__(self):
        self.conn = sql.connect(os.environ["DATABASE_URL"], sslmode="require")
        #self.conn = sql.connect("game.db")
        self.active_players = {}
        self.create_tables()
        self.populate_players()

    def command_list(self):
        admin_commands = {
            "register": {"player": {"base": self.register_player}}
        }
        view_commands = {
            "summary": self.view_base,
            "shop": self.view_shop
        }
        build_commands = {
            "generator": self.build_generator,
            "armory": self.build_armory
        }
        hire_commands = {
            "soldier": self.hire_soldier
        }
        buy_commands = {
            "sword": self.buy_sword
        }
        base_commands = {
            "view": view_commands,
            "build": build_commands,
            "buy": buy_commands,
            "hire": hire_commands
        }
        top_level = {
            "!base": base_commands,
            "!check_gold": self.check_gold,
            "!gather_gold": self.gather_gold
        }
        return top_level

    def check_registration(self, player_name):
        if player_name not in self.active_players.keys():
            return False, "You are not registered, please contact an admin to register"
        else:
            return True, ""

    def register_player(self, admin_name: int, player_name: str, player_id):
        player_id = str(player_id)
        if admin_name not in ADMIN_LIST:
            return "Invalid access, you are not an admin"
        c = self.conn.cursor()
        c.execute("INSERT INTO players VALUES (%s,%s,%s,3)", (player_id, player_name, 0))
        for item_name in ITEMS_SQL.keys():
            c.execute("INSERT INTO items VALUES (%s, %s, %s)", (player_id, item_name, 0))
        try:
            self.conn.commit()
        except Exception as e:
            print(e)
            print(e.pgerror)
            sys.stdout.flush()
            self.conn.rollback()
        else:
            self.conn.commit()
        for unit_name in UNITS_SQL.keys():
            c.execute("INSERT INTO garrison VALUES (%s, %s, %s)", (player_id, unit_name, 0))
        try:
            self.conn.commit()
        except Exception as e:
            print(e)
            print(e.pgerror)
            sys.stdout.flush()
            self.conn.rollback()
            sys.stdout.flush()
        else:
            self.conn.commit()
        for building_name in BUILDINGS_SQL.keys():
            c.execute("INSERT INTO buildings VALUES (%s, %s, %s)", (player_id, building_name, 0))
        try:
            self.conn.commit()
        except Exception as e:
            print(e)
            print(e.pgerror)
            sys.stdout.flush()
            self.conn.rollback()
        else:
            self.conn.commit()
        base = Base(generators=[Generator(), Generator(), Generator()])
        self.active_players[player_name] = Player(player_name, base, player_id)
        return "Player registered, {} registered!".format(player_name)

    def populate_players(self):
        player_cur = self.conn.cursor()
        player_cur.execute("SELECT player_id, name, gold, generators FROM players")
        try:
            self.conn.commit()
        except Exception as e:
            print(e)
            print(e.pgerror)
            sys.stdout.flush()
            self.conn.rollback()
        else:
            self.conn.commit()
        player_list = player_cur.fetchall()
        if player_list:
            for player in player_list:
                player_id = player[0]
                player_name = player[1]
                player_gold = player[2]
                player_generators = player[3]
                player_buildings = []
                items, buildings, garrison = self.load_player(player_id)
                generators = [Generator()] * player_generators
                base = Base(garrison=garrison, buildings=buildings, generators=generators, items=items)
                player_obj = Player(player_name, base, player_id)
                self.active_players[player_name] = player_obj

    def load_player(self, player_id):
        items = self.get_items(player_id)
        buildings = self.get_buildings(player_id)
        garrison = self.get_garrison(player_id)
        return items, buildings, garrison

    def get_buildings(self, player_id):
        cur = self.conn.cursor()
        cur.execute("SELECT building, amount FROM buildings WHERE player_id = %s", (player_id,))
        all_buildings = cur.fetchall()
        player_buildings = []
        for building in all_buildings:
            if building[1]:
                building_name = building[0]
                building_obj = BUILDINGS_SQL[building_name]
                player_buildings.extend([building_obj() for i in range(building[1])])
        return player_buildings

    def get_items(self, player_id):
        cur = self.conn.cursor()
        cur.execute("SELECT item, amount FROM items WHERE player_id = %s", (player_id,))
        items = cur.fetchall()
        player_items = []
        for item in items:
            if item[1]:
                item_name = item[0]
                item_obj = ITEMS_SQL[item_name]
                player_items.extend([item_obj() for i in range(item[1])])
        return player_items

    def get_garrison(self, player_id):
        cur = self.conn.cursor()
        cur.execute("SELECT unit, amount FROM garrison WHERE player_id = %s", (player_id,))
        units = cur.fetchall()
        player_units = []
        for unit in units:
            if unit[1]:
                unit_id = unit[0]
                unit_obj = UNITS_SQL[unit_id]
                player_units.extend([unit_obj() for i in range(unit[1])])
        return player_units

    def save_table(self, table_name, player_id, component_name, number):
        c = self.conn.cursor()
        try:
            c.execute(
            sql.SQL("UPDATE {} SET amount = %s WHERE player_id = %s and name = %s")
                .format(sql.Identifier(table_name)),
            (number, player_id, component_name))
            self.conn.commit()
        except Exception as e:
            print(e)
            print(e.pgerror)
            sys.stdout.flush()
            self.conn.rollback()
            return "In save_table {}, table: {}".format(e.pgerror, table_name)
        else:
            self.conn.commit()
        return True

    def save_buildings(self, player_id, base):
        buildings = {}
        for building in base.buildings:
            if building.name in buildings:
                buildings[building.name] += 1
            else:
                buildings[building.name] = 1
        for building in buildings.keys():
            num = buildings[building]
            self.save_table('buildings', player_id, building, num)
            
    def save_garrison(self, player_id, base):
        garrison = {}
        for unit in base.garrison:
            if unit.name in garrison:
                garrison[unit.name] += 1
            else:
                garrison[unit.name] = 1
        for unit in garrison.keys():
            num = garrison[unit]
            self.save_table('garrison', player_id, unit, num)

    def save_items(self, player_id, base):
        items = {}
        for item in base.items:
            if item.name in items:
                items[item.name] += 1
            else:
                items[item.name] = 1
        for item in items.keys():
            num = items[item]
            self.save_table('items', player_id, item, num)


    def save_player(self, player):
        base = player.base
        player_id = str(player.id)
        name = player.name
        garrison = base.garrison
        items = base.items
        generators = len(base.generators)
        self.save_buildings(player_id, base)
        self.save_garrison(player_id, base)
        self.save_items(player_id, base)
        try:
            c = self.conn.cursor()
            c.execute("UPDATE players SET generators = %s WHERE player_id = %s", (generators, player_id))
            self.conn.commit()
        except Exception as e:
            print(e)
            print(e.pgerror)
            sys.stdout.flush()
            self.conn.rollback()
            return "In save_player {}".format(e.pgerror)
        else:
            self.conn.commit()

    def save_players(self):
        for player in self.active_players.values():
            self.save_player(player)
        return None

    def create_tables(self):
        # c = self.conn.cursor()
        # c.execute('''DROP TABLE IF EXISTS players''')
        # c.execute('''DROP TABLE IF EXISTS items''')
        # c.execute('''DROP TABLE IF EXISTS buildings''')
        # c.execute('''DROP TABLE IF EXISTS garrison''')
        # try:
        #     self.conn.commit()
        # except Exception as e:
        #     print(e)
        #     print(e.pgerror)
        #     sys.stdout.flush()
        #     self.conn.rollback()
        # else:
        #     self.conn.commit()
        try:
            c = self.conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS players
                                                (player_id varchar PRIMARY KEY, name varchar, gold integer, generators integer)''')
            c.execute('''CREATE TABLE IF NOT EXISTS items
                                                (player_id varchar, item varchar, amount integer)''')
            c.execute('''CREATE TABLE IF NOT EXISTS buildings
                                                (player_id varchar, building varchar, amount integer)''')
            c.execute('''CREATE TABLE IF NOT EXISTS garrison
                                                (player_id varchar, unit varchar, amount integer)''')
            self.conn.commit()
        except Exception as e:
            print(e)
            print(e.pgerror)
            sys.stdout.flush()
            self.conn.rollback()
        else:
            self.conn.commit()

    def get_player(self, player_name):
        for player in self.active_players.values():
            if player_name == player.name:
                return player

    def can_afford(self, player, cost):
        c = self.conn.cursor()
        gold = player.check_gold(c)
        if gold >= cost:
            gold -= cost
            self.set_gold(player.id, gold)
            return True, gold
        else:
            return False, gold

    def check_gold(self, player_name):
        c = self.conn.cursor()
        player = self.get_player(player_name)
        gold = player.check_gold(c)
        return gold

    def build_generator(self, player_name):
        player = self.get_player(player_name)
        can_build, gold = self.can_afford(player, GENERATOR_COST)
        if can_build:
            player.base.build_generator()
            return "You built a generator, you now have {} {}".format(gold, GOLD_COIN)
        else:
            return "You do not have enough to build a generator, you have {} {}".format(gold, GOLD_COIN)

    def build_armory(self, player_name):
        player = self.get_player(player_name)
        can_build, gold = self.can_afford(player, ARMORY_COST)
        if can_build:
            player.base.build_armory()
            return "You built an armory, you now have {} {}".format(gold, GOLD_COIN)
        else:
            return "You do not have enough to build an armory, you have {} {}".format(gold, GOLD_COIN)

    def buy_sword(self, player_name: str, item="sword") -> str:
        return self.buy_item(player_name, item)

    def buy_item(self, player_name, item):
        item = item.lower()
        if item not in ITEM_PRICE_MAP:
            return "Item not recognized"
        player = self.get_player(player_name)
        can_build, gold = self.can_afford(player, ITEM_PRICE_MAP[item])
        if can_build:
            success = player.base.buy_item(item)
            if success:
                return "You bought a {}, you now have {} {}".format(item, gold, GOLD_COIN)
            else:
                return "Cannot buy {}, that item is not available to you".format(item)
        else:
            return "You do not have enough to build a {}, you have {} {}".format(item, gold, GOLD_COIN)

    def hire_soldier(self, player_name):
        player = self.get_player(player_name)
        can_build, gold = self.can_afford(player, SOLDIER_COST)
        if can_build:
            player.base.hire_soldier()
            return "You hired a soldier, you now have {} {}".format(gold, GOLD_COIN)
        else:
            return "You do not have enough to hire a soldier, you have {} {}".format(gold, GOLD_COIN)

    def view_base(self, player_name):
        player = self.get_player(player_name)
        return player.base.view_base()

    def view_shop(self, player_name):
        player = self.get_player(player_name)
        return player.base.view_shop()

    def gather_gold(self, player_name):
        player = self.get_player(player_name)
        gold_gained = player.base.empty_generators()
        c = self.conn.cursor()
        c.execute("SELECT gold FROM players WHERE name = %s", (player_name,))
        total_gold = c.fetchone()[0]
        total_gold += gold_gained
        c.execute("UPDATE players SET gold = %s WHERE player_id = %s", (total_gold, player.id))
        try:
            self.conn.commit()
        except Exception as e:
            print(e)
            print(e.pgerror)
            sys.stdout.flush()
            self.conn.rollback()
        else:
            self.conn.commit()
        return "You have {} gold, you've gained {} gold since your last check".format(total_gold, gold_gained)

    def gather_gold_all(self):
        for player_name in self.active_players.keys():
            self.gather_gold(player_name)
        return True

    def set_gold(self, player_id, total_gold):
        c = self.conn.cursor()
        c.execute("UPDATE players SET gold = %s WHERE player_id = %s", (total_gold, player_id))
        try:
            self.conn.commit()
        except Exception as e:
            print(e)
            print(e.pgerror)
            sys.stdout.flush()
            self.conn.rollback()
        else:
            self.conn.commit()

    def battle(self, offense_units: Army, defense_units: Army):
        offense_unit = offense_units.next()
        defense_unit = defense_units.next()
        offense_win = None
        while offense_units.men_remaining() and defense_units.men_remaining():
            offense_win = self.fight(offense_unit, defense_unit)
            if offense_win:
                defense_unit = defense_units.next()
            else:
                offense_unit = offense_units.next()
        offense_units_lost = offense_units.clear_dead()
        defense_units_lost = defense_units.clear_dead()
        return offense_units_lost, defense_units_lost, offense_win

    def fight(self, offense_unit: Man, defense_unit: Man):
        defense_ttk = self._get_ttk(defense_unit, offense_unit)
        offense_ttk = self._get_ttk(offense_unit, defense_unit)
        if offense_ttk < defense_ttk:
            self.fight_results(offense_unit, defense_unit, offense_ttk)  # offense win
            return True
        else:
            self.fight_results(defense_unit, offense_unit, defense_ttk)  # defense win
            return False

    def fight_results(self, winning_unit, losing_unit, winning_ttk):
        losing_unit.kill()
        losing_damage = math.floor(winning_ttk * losing_unit.damage)
        if losing_damage == winning_unit.health:
            losing_damage = math.floor(winning_unit.health * .1)
        winning_unit.injure(losing_damage)

    def _get_ttk(self, attacking_unit: Man, defending_unit: Man):
        swings = defending_unit.health() // attacking_unit.damage
        if defending_unit.health() % swings:
            swings += 1
        ttk = swings / attacking_unit.attack_speed
        return ttk


class Player(object):
    def __init__(self, name, base, id):
        self.name = name
        self.base = base
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be none or empty")
        self._name = value

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    def check_gold(self, c):
        c.execute("SELECT gold FROM players WHERE name = %s", (self.name,))
        return c.fetchone()[0]
