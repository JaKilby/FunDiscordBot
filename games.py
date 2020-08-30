import random

DIAMOND = u':small_blue_diamond:'
ORANGE_DIAMOND = u':small_orange_diamond:'
PIRATE_FLAG = u':pirate_flag:'
BEER = u':beer:'
ICECREAM = u':icecream:'
PERSON_FENCING = u':person_fencing:'
CROISSANT = u':croissant:'
WATERMELON = u':watermelon:'
SNOWBOARDER = u':snowboarder:'
SPIDER_WEB = u':spider_web:'
EMOJIS = [DIAMOND, PIRATE_FLAG, BEER, ICECREAM, PERSON_FENCING, CROISSANT,
          WATERMELON, SNOWBOARDER, SPIDER_WEB, ORANGE_DIAMOND]


class Games(object):
    def __init__(self, credit_manager):
        self.credit_manager = credit_manager

    def high_low(self, guess):
        pick = random.randint(1, 12)
        if guess == "high" and pick > 6:
            return True, pick
        elif guess == "low" and pick < 6:
            return True, pick
        elif guess == "even" and pick == 6:
            return True, pick
        else:
            return False, pick

    def slots(self):
        selected = []
        for i in range(3):
            row = []
            for j in range(3):
                rand_choice = random.randint(0, 8)
                row.append(EMOJIS[rand_choice])
            selected.append(row)
        slot_str = u''
        for row in selected:
            row_str = u''
            for emoji in row:
                row_str += emoji
            row_str += u'\n'
            slot_str += row_str
        if selected[1][0] == selected[1][1] == selected[1][2]:
            win = True
        else:
            win = False
        return win, u'{}'.format(slot_str)

