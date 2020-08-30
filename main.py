# This is a sample Python script.
import discord
import os
import random
from tictactoe import TicTacToe
from credits_manager import CreditManager
from games import Games
from queue import Queue
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class MyClient(discord.Client):
    def handle_commands(self, message):
        if message.content == "!games":
            return "@everyone val or fallguys?"
        elif message.content == "!fallguys":
            ascii_art = ("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠉⠉⠉⠉⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                         "⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⢀⣠⣶⣶⣶⣶⣤⡀⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿\n"
                         "⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⣾⡿⢿⣿⣿⡿⢿⣿⡆⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿\n"
                         "⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⠄⢿⣇⣸⣿⣿⣇⣸⡿⠃⠄⠄⠸⣿⣿⣿⣿⣿⣿⣿\n"
                         "⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⠄⠄⠉⠛⠛⠛⠛⠉⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿\n"
                         "⣿⣿⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣿⣿\n"
                         "⣿⣿⣿⡟⠄⠄⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢿⣿⣿\n"
                         "⣿⣿⡟⠄⠄⠄⢠⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣧⠄⠄⠄⠈⢿⣿\n"
                         "⣿⣿⡇⠄⠄⠄⣾⣿⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣧⠄⠄⠄⠘⣿\n"
                         "⣿⣿⣇⠄⣰⣶⣿⣿⣿⣦⣀⡀⠄⠄⠄⠄⠄⠄⠄⢀⣠⣴⣿⣿⣿⣶⣆⠄⢀⣿\n"
                         "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⢸⣿⠇⠄⠄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                         "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣴⣾⣿⣶⣤⣤⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n")
            return ascii_art
        elif message.content == "!reverse":
            ascii_art = ("```\n"
                         "⠐⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠂\n"
                         "⠄⠄⣰⣾⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠄⠄\n"
                         "⠄⠄⣿⣿⣿⡿⠋⠄⡀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⣉⣉⣉⡉⠙⠻⣿⣿⠄⠄\n"
                         "⠄⠄⣿⣿⣿⣇⠔⠈⣿⣿⣿⣿⣿⡿⠛⢉⣤⣶⣾⣿⣿⣿⣿⣿⣿⣦⡀⠹⠄⠄\n"
                         "⠄⠄⣿⣿⠃⠄⢠⣾⣿⣿⣿⠟⢁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄\n"
                         "⠄⠄⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⠄\n"
                         "⠄⠄⣿⣿⣿⣿⣿⡟⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄\n"
                         "⠄⠄⣿⣿⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄\n"
                         "⠄⠄⣿⣿⡿⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⠗⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⡟⠄⠄\n"
                         "⠄⠄⣿⡿⠁⣼⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⣠⣄⢰⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄\n"
                         "⠄⠄⡿⠁⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⢀⡴⠚⢿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⠄⠄\n"
                         "⠄⠄⠃⢰⣿⣿⣿⣿⣿⣿⡿⣿⣿⠴⠋⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⠄⠄\n"
                         "⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⠃⠈⠁⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿⠄⠄\n"
                         "⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢶⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⣾⣿⣿⠄⠄\n"
                         "⠄⠄⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠋⣠⣿⣿⣿⣿⠄⠄\n"
                         "⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣼⣿⣿⣿⣿⣿⠄⠄\n"
                         "⠄⠄⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⠄⠄\n"
                         "⠄⠄⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣴⣿⣿⣿⣿⠗⠄⠄⣿⣿⠄⠄\n"
                         "⠄⠄⣆⠈⠻⢿⣿⣿⣿⣿⣿⣿⠿⠛⣉⣤⣾⣿⣿⣿⣿⣿⣇⠠⠺⣷⣿⣿⠄⠄\n"
                         "⠄⠄⣿⣿⣦⣄⣈⣉⣉⣉⣡⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⠉⠁⣀⣼⣿⣿⣿⠄⠄\n"
                         "⠄⠄⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⡿⠟⠄⠄\n"
                         "⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
                         "```")
            return ascii_art
        elif message.content == "!risk":
            return "The dice hate me!"
        elif message.content == "!tictactoe":
            self.tic_tac_toe = not self.tic_tac_toe
            if self.tic_tac_toe:
                self.player1 = None
                self.player2 = None
                self.players_set = False
                return "Starting tic tac toe, player1 say \"me\""
            else:
                return "Exiting tic tac toe"
        elif "!give" in message.content:
            if message.author.name != "kilbo":
                return "Not authorized"
            else:
                credit_statement = message.content.split()
                player = credit_statement[1]
                credits = int(credit_statement[2])
                self.manager.give_credits(player, credits)
                if credits > 0:
                    return "Gave {} credits to {}".format(credits, player)
                else:
                    return "Took {} credits from {}".format(abs(credits), player)
        elif "!check_credits" in message.content:
            credit_statement = message.content.split()
            player = credit_statement[1]
            credits = self.manager.check_credits(player)
            if credits == 0:
                return "{} is broke.".format(player)
            return "{} has {} credits".format(player, credits)
        elif "!check_balance" == message.content:
            return "You have {} credits".format(self.manager.check_credits(message.author.name))
        elif message.content.split()[0] == "!highlow":
            game_str = message.content.split()
            if len(game_str) > 3:
                return "Please use format \"!highlow guess wager\""
            guess = game_str[1]
            if guess not in ["even", "high", "low"]:
                return "Guess must be one of [even, high, low]"
            wager = game_str[2]
            if wager.isnumeric():
                wager = int(wager)
            else:
                return "Please only wager positive, whole numbers."
            player_credits = self.manager.check_credits(message.author.name)
            if wager > player_credits:
                return "Cannot wager more credits than you have."
            win, roll = self.game_manager.high_low(guess)
            roll_statement = "The roll was: {}\n".format(roll)
            if not win:
                self.manager.give_credits(message.author.name, -wager)
                return roll_statement + "You lost {} credits".format(wager)
            else:
                if guess == "even":
                    wager = wager * 2
                self.manager.give_credits(message.author.name, wager)
                return roll_statement + "You won {} credits".format(wager)
        elif message.content == "!emojis" and message.author.name == "kilbo":
            emojis = self.emojis
            emoji_ids = [(str(emoji.id), emoji.name) for emoji in emojis]
            worked = "No"
            worked = self.manager.save_emojis(emoji_ids)
            return worked
        elif message.content.lower() == "!help":
            return "Available commands:\n    !fallguys\n    !games\n    !fishtime\n    !tictactoe\n    !highlow\n    !check_credits\n    !check_balance"

    async def on_ready(self):
        self.tic_tac_toe = False
        self.players_set = False
        self.current_turn = None
        self.game_client = None
        self.player1 = None
        self.player2 = None
        self.turn_queue = Queue()
        self.manager = CreditManager()
        self.game_manager = Games(self.manager)
        self.manager.create_table()
        print("Logged on as {}".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))

        rand_int = random.randint(0, 100)
        if message.author.name == "gmink" and rand_int % 20 == 0:
            await message.channel.send("shut up console nerd")
        elif message.author.name == "ABakedFish" and "ABakedFish" not in [self.player1, self.player2]:
            fish_int = random.randint(0, 5)
            if "fall" in message.content.lower():
                await message.channel.send("lEtS pLaY fAlL gUyS")
            elif "@" in message.content and fish_int % 2 == 0:
                await message.channel.send("Fish wants to game? ITS FISHTIME!!!!")
                await message.channel.send("!fishtime")
        if message.content[0] == "!":
            if message.content == "!fishtime":
                fishtime_str = "<:FishEmote:742769011833438241> " * 10 + "\n" + "<:FishEmote:742769011833438241> " * 10
                await message.channel.send(fishtime_str)
                await message.channel.send(fishtime_str)
                await message.channel.send(fishtime_str)
                await message.channel.send(fishtime_str)
                await message.channel.send(fishtime_str)
            else:
                await message.channel.send(self.handle_commands(message))
        elif self.tic_tac_toe:
            if not self.players_set:
                if message.content == "me":
                    if self.player1 is None:
                        self.player1 = message.author.name
                        await message.channel.send("Player 2 say \"me\"")
                    elif self.player2 is None:
                        self.player2 = message.author.name
                        self.players_set = True
                        self.current_turn = self.player1
                        while not self.turn_queue.empty():
                            self.turn_queue.get()
                        self.turn_queue.put(self.player2)
                        self.game_client = TicTacToe(self.player1, self.player2)
                        await message.channel.send("Player 1 is: {}\nPlayer 2 is: {}\nPlayer 1 starts".format(self.player1, self.player2))
                    else:
                        await message.channel.send("Game is full")
            else:
                if message.author.name == self.player1 or message.author.name == self.player2:
                    if message.author.name == self.current_turn:
                        move = message.content
                        if self.game_client.validate_move(move):
                            resp = self.game_client.make_move(self.current_turn, move)
                            if "wins" in resp:
                                await message.channel.send(resp)
                                self.tic_tac_toe = False
                                return
                            self.turn_queue.put(self.current_turn)
                            self.current_turn = self.turn_queue.get()
                            await message.channel.send(resp)
                            await message.channel.send("{} it is now your turn.".format(self.current_turn))
                    else:
                        await message.channel.send("It is {}'s turn".format(self.current_turn))



def main():
    client = MyClient()
    client.run(os.environ['DISCORD_TOKEN'])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
