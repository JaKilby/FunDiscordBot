import asyncio
import time
import datetime

async def test1():
    print(datetime.datetime.now())
    time.sleep(10)
    print("test1")
    print(datetime.datetime.now())


async def test2():
    print(datetime.datetime.now())
    time.sleep(15)
    print("test2")
    print(datetime.datetime.now())


async def main():
    asyncio.gather(test1(), test2())



asyncio.run(main())