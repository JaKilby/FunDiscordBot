# This is a sample Python script.
import discord
import os
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class MyClient(discord.Client):
    async def on_read(self):
        print("Logged on as {}".format(self.user))

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))
        #<:FishEmote: 742769011833438241 >
        rand_int = random.randint(0,100)
        if message.author.name == "gmink" and rand_int == 50:
            await message.channel.send("shut up console nerd")
        elif message.author.name == "ABakedFish":
            if "fall" in message.content.lower():
                await message.channel.send("LeTs PlAy FaLl GuYs")
            elif "@" in message.content:
                await message.channel.send("Fish wants to game? ITS FISHTIME!!!!")
                await message.channel.send("!fishtime")
        elif message.content == "!games":
            await message.channel.send("@everyone val or fallguys?")
        elif message.content == "!fishtime":
            fishtime_str = "<:FishEmote:742769011833438241> " * 10 +"\n" + "<:FishEmote:742769011833438241> " * 10
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
        elif message.content.lower() == "!help":
            await message.channel.send("Available commands:\n    !fallguys\n    !games\n    !fishtime")


def main():
    client = MyClient()
    client.run(os.environ['DISCORD_TOKEN'])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
