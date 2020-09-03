PLAYER1_TILE = "X"
PLAYER2_TILE = "O"
EMPTY_TILE = " "
ROW_SEPERATOR = "-----------\n"
ROW = "{} |  {}  | {}\n"
TOP_LEFT = (0, 0)
TOP_MIDDLE = (0, 1)
TOP_RIGHT = (0, 2)
MIDDLE_LEFT = (1, 0)
MIDDLE_MIDDLE = (1, 1)
MIDDLE_RIGHT = (1, 2)
BOTTOM_LEFT = (2, 0)
BOTTOM_MIDDLE = (2, 1)
BOTTOM_RIGHT = (2, 2)
MOVE_DICT = {
    "top left": TOP_LEFT,
    "tl": TOP_LEFT,
    "top middle": TOP_MIDDLE,
    "tm": TOP_MIDDLE,
    "top right": TOP_RIGHT,
    "tr": TOP_RIGHT,
    "middle_left": MIDDLE_LEFT,
    "ml": MIDDLE_LEFT,
    "middle middle": MIDDLE_MIDDLE,
    "mm": MIDDLE_MIDDLE,
    "middle right": MIDDLE_RIGHT,
    "mr": MIDDLE_RIGHT,
    "bottom left": BOTTOM_LEFT,
    "bl": BOTTOM_LEFT,
    "bottom middle": BOTTOM_MIDDLE,
    "bm": BOTTOM_MIDDLE,
    "bottom right": BOTTOM_RIGHT,
    "br": BOTTOM_RIGHT
}
NED = ("```▄▄▄▄▄▄▄▄▄\n"
"░▄███████▀▀▀▀▀▀███████▄\n"
"░▐████▀▒DIDDLY▒▒▒▒▀██████▄\n"
"░███▀▒▒▒▒SPAMLY▒▒▒▒▒▀█████\n"
"░▐██▒▒▒▒▒▒DOODLY▒▒▒▒▒▒████▌\n"
"░▐█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▌\n"
"░░█▒▄▀▀▀▀▀▄▒▒▄▀▀▀▀▀▄▒▐███▌\n"
"░░░▐░░░▄▄░░▌▐░░░▄▄░░▌▐███▌\n"
"░▄▀▌░░░▀▀░░▌▐░░░▀▀░░▌▒▀▒█▌\n"
"░▌▒▀▄░░░░▄▀▒▒▀▄░░░▄▀▒▒▄▀▒▌\n"
"░▀▄▐▒▀▀▀▀▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒█\n"
"░░░▀▌▒▄██▄▄▄▄████▄▒▒▒▒█▀\n"
"░░░░▄██████████████▒▒▐▌\n"
"░░░▀███▀▀████▀█████▀▒▌\n"
"░░░░░▌▒▒▒▄▒▒▒▄▒▒▒▒▒▒▐\n"
"░░░░░▌▒▒▒▒▀▀▀▒▒▒▒▒▒▒▐```\n")

SURPRISE = ("⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿\n"
"⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿\n"
"⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿\n"
"⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿")


#GOLD_COIN = "<:gold_coin:749962304065372182>"
GOLD_COIN = "<:gold_coin:749933893490311228>"
GENERATOR_COST = 10000
SOLDIER_COST = 1000
SWORD_COST = 500
SHIELD_COST = 750
ARMORY_COST = 15000
BASE_GENERATOR_GOLD = 10000
MAX_GOLD_STORED = 1000
ITEM_PRICE_MAP = {
    "sword": SWORD_COST,
    "shield": SHIELD_COST
}

