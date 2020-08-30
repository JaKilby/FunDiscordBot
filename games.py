import random

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
