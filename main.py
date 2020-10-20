# This is a sample Python script.
import discord
import os
import random
from tictactoe import TicTacToe
from credits_manager import CreditManager
from raiders import RaidersManager
from constants import NED, SURPRISE
from games import Games
from queue import Queue
import datetime
import asyncio
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#dl
class GameClient(discord.Client):
    async def gold_gatherer(self):
        while True:
            await asyncio.sleep(300)
            self.manager.gather_gold_all()
            result = self.manager.save_players()
            if result:
                await self.get_channel(749847611971731496).send(result)
            await self.get_channel(749847611971731496).send("Gathered gold and saved at {}".format(datetime.datetime.now()))

    async def on_ready(self):
        print("Logged in as game manager client")
        self.manager = RaidersManager()
        self.command_list = self.manager.command_list()
        asyncio.create_task(self.gold_gatherer())

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))
        name = message.author.name
        if message.content.lower() == "can i get a big mac?":
            await message.channel.send("Breakfast Fruit & Maple Oatmeal Fruit 'N Yogurt Parfait Egg McMuffin® Egg White Delight McMuffin® Sausage McMuffin® Sausage McMuffin® with Egg Bacon, Egg & Cheese Biscuit Sausage Biscuit Sausage Biscuit with Egg Steak, Egg & Cheese Biscuit Bacon, Egg & Cheese McGriddles® Sausage McGriddles® Sausage, Egg & Cheese McGriddles® Bacon, Egg & Cheese Bagel Big Breakfast® Big Breakfast® with Hotcakes Hotcakes Hotcakes and Sausage Sausage Burrito Hash Browns Burgers Bacon Smokehouse Burger Double Bacon Smokehouse Burger Big Mac® Quarter Pounder®* with Cheese Double Quarter Pounder®* with Cheese Triple Cheeseburger Double Cheeseburger McDouble® Bacon McDouble® Cheeseburger Hamburger Chicken & Sandwiches Bacon Smokehouse Buttermilk Crispy Chicken Bacon Smokehouse Artisan Grilled Chicken 4 piece Chicken McNuggets® Buttermilk Crispy Tenders Classic Chicken Sandwich Artisan Grilled Chicken Sandwich Buttermilk Crispy Chicken Sandwich McChicken® Filet-O-Fish® Bacon Ranch Salad with Buttermilk Crispy Chicken Bacon Ranch Grilled Chicken Salad Southwest Buttermilk Crispy Chicken Salad Southwest Grilled Chicken Salad Salads Bacon Ranch Salad with Buttermilk Crispy Chicken Bacon Ranch Grilled Chicken Salad Southwest Buttermilk Crispy Chicken Salad Southwest Grilled Chicken Salad Side Salad Snacks & Sides World Famous Fries® Yoplait® GO-GURT® Low Fat Strawberry Yogurt Fruit 'N Yogurt Parfait Desserts & Shakes Chocolate Shake Strawberry Shake Vanilla Shake Vanilla Cone Hot Fudge Sundae McFlurry® with M&M'S® Candies Kiddie Cone Hot Caramel Sundae Strawberry Sundae McFlurry® with OREO® Cookies Baked Apple Pie Strawberry & Crème Pie Chocolate Chip Cookie Oatmeal Raisin Cookie Drinks MIX by Sprite™ Tropic Berry Hot Chocolate Coca-Cola® Chocolate Shake Strawberry Shake")

        if message.channel.name == "raiders-preview" and message.author.name != "minkowbadbot":
            if message.content[0] == "!":
                commands = message.content.lower().split()
                if commands[0] == "!register":
                    first_char = message.content.find("<") + 3
                    second_char = message.content.find(">")
                    player_id = message.content[first_char:second_char]
                    await message.channel.send("Player ID {}".format(player_id))
                    msg = self.manager.register_player(message.author.id, commands[3], player_id)
                    await message.channel.send(msg)
                    return
                registered, msg = self.manager.check_registration(name)
                if not registered:
                    await message.channel.send(msg)
                    return
                pointer = self.command_list
                for command in commands:
                    pointer = pointer[command]
                    if callable(pointer):
                        break
                else:
                    await message.channel.send("Command not recognized")
                    return
                result = pointer(name)
                await message.channel.send(result)



def main():
    #client = MyClient()
    client = GameClient()
    client.run(os.environ['DISCORD_TOKEN'])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
