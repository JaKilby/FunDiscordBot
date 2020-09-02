import psycopg2 as sql
#import sqlite3 as sql
import os
import datetime
import math

#import threading.lock

import uuid
from units import Man, Army
from buildings import Building, Generator
from constants import GOLD_COIN, GENERATOR_COST, SOLDIER_COST, ARMORY_COST, ITEM_PRICE_MAP
from base import Base, BUILDINGS_SQL
from items import ITEMS_SQL
from units import UNITS_SQL

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
        if admin_name not in ADMIN_LIST:
            return "Invalid access, you are not an admin"
        c = self.conn.cursor()
        c.execute("INSERT INTO players VALUES (%s,%s,%s,3)", (player_id, player_name, 0))
        self.conn.commit()
        base = Base(generators=[Generator(), Generator(), Generator()])
        self.active_players[player_name] = Player(player_name, base, player_id)
        return "Player registered, {} registered!".format(player_name)

    def populate_players(self):
        player_cur = self.conn.cursor()
        player_list = player_cur.execute("SELECT id, name, gold, generators FROM players")
        if player_list is not None:
            player_list = player_list.fetchall()
        for player in player_list:
            player_id = player[0]
            player_name = player[1]
            player_gold = player[2]
            player_generators = player[3]
            player_buildings = []
            cur = self.conn.cursor()
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
        cur.execute("SELECT building FROM buildings WHERE id = %s", (player_id,))
        all_buildings = cur.fetchall()
        player_buildings = []
        for building in all_buildings:
            building_name = building[1]
            building = BUILDINGS_SQL[building_name]()
            player_buildings.append(player_buildings)
        return player_buildings

    def get_items(self, player_id):
        cur = self.conn.cursor()
        cur.execute("SELECT item FROM items WHERE id = %s", (player_id,))
        items = cur.fetchall()
        player_items = []
        for item in items:
            item_name = item[0]
            item = ITEMS_SQL[item_name]()
            player_items.append(item)
        return player_items

    def get_garrison(self, player_id):
        cur = self.conn.cursor()
        cur.execute("SELECT unit FROM garrison WHERE id = %s", (player_id,))
        units = cur.fetchall()
        player_units = []
        for unit in units:
            unit_id = unit[0]
            unit = UNITS_SQL[unit_id]()
            player_units.append(unit)
        return player_units

    def save_table(self, table_name, player_id, components):
        c = self.conn.cursor()
        for component in components:
            c.execute(
                sql.SQL("insert into {} values (%s, %s)")
                    .format(sql.Identifier(table_name)),
                (player_id, component.name))
        self.conn.commit()
        return True

    def save_player(self, player):
        base = player.base
        id = player.id
        name = player.name
        garrison = base.garrison
        items = base.items
        generators = len(base.generators)
        buildings = base.buildings
        self.save_table('buildings', base.buildings)
        self.save_table('items', base.items)
        self.save_table('garrison', base.garrison)
        c = self.conn.cursor()
        c.execute("UPDATE players SET gold = %s WHERE player_id = %s", (player.gold, player.id))
        c.execute("UPDATE players SET generators = %s WHERE player_id = %s", (generators, player.id))
        self.conn.commit()

    def save_players(self):
        for player in self.active_players.values():
            self.save_player(player)
        return True

    def create_tables(self):
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS players
                                            (id varchar PRIMARY KEY, name varchar, gold integer, generators integer)''')
        c.execute('''CREATE TABLE IF NOT EXISTS items
                                            (id varchar, item varchar)''')
        c.execute('''CREATE TABLE IF NOT EXISTS buildings
                                            (id varchar, building varchar)''')
        c.execute('''CREATE TABLE IF NOT EXISTS garrison
                                            (id varchar, unit varchar)''')
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
        c.execute("UPDATE players SET gold = %s WHERE id = %s", (total_gold, player.id))
        self.conn.commit()
        return "You have {} gold, you've gained {} gold since your last check".format(total_gold, gold_gained)

    def gather_gold_all(self):
        for player_name in self.active_players.keys():
            self.gather_gold(player_name)
        return True

    def set_gold(self, player_id, total_gold):
        c = self.conn.cursor()
        c.execute("UPDATE players SET gold = %s WHERE id = %s", (total_gold, player_id))
        self.conn.commit()

    def battle(self, offense_units: Army, defense_units: Army):
        offense_unit = offense_units.next()
        defense_unit = defense_units.next()
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
