# This is a sample Python script.
import discord
import os
import random
from tictactoe import TicTacToe
from queue import Queue
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class MyClient(discord.Client):
    async def on_ready(self):
        self.tic_tac_toe = False
        self.players_set = False
        self.current_turn = None
        self.game_client = None
        self.player1 = None
        self.player2 = None
        self.turn_queue = Queue()
        print("Logged on as {}".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))

        rand_int = random.randint(0, 100)
        if message.author.name == "gmink" and rand_int % 20 == 0:
            await message.channel.send("shut up console nerd")
        elif message.author.name == "ABakedFish" and "ABakedFish" not in [self.player1, self.player2]:
            fish_int = random.randint(0,5)
            if "fall" in message.content.lower():
                await message.channel.send("lEtS pLaY fAlL gUyS")
            elif "@" in message.content and fish_int % 2 == 0:
                await message.channel.send("Fish wants to game? ITS FISHTIME!!!!")
                await message.channel.send("!fishtime")
        if message.content[0] == "!":
            if message.content == "!games":
                await message.channel.send("@everyone val or fallguys?")
            elif message.content == "!fishtime":
                fishtime_str = "<:FishEmote:742769011833438241> " * 10 + "\n" + "<:FishEmote:742769011833438241> " * 10
                await message.channel.send(fishtime_str)
                await message.channel.send(fishtime_str)
                await message.channel.send(fishtime_str)
                await message.channel.send(fishtime_str)
                await message.channel.send(fishtime_str)
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
                await message.channel.send(ascii_art)
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
                await message.channel.send(ascii_art)
            elif message.content == "!risk":
                await message.channel.send("The dice hate me!")
            elif message.content == "!tictactoe":
                self.tic_tac_toe = not self.tic_tac_toe
                if self.tic_tac_toe:
                    self.player1 = None
                    self.player2 = None
                    self.players_set = False
                    await message.channel.send("Starting tic tac toe, player1 say \"me\"")
                else:
                    await message.channel.send("Exiting tic tac toe")
            elif message.content.lower() == "!help":
                await message.channel.send(
                    "Available commands:\n    !fallguys\n    !games\n    !fishtime\n    !tictactoe")
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
