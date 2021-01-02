from settings import Connection
from pprint import pprint
import asyncio


users = Connection().get_db().users


async def find():

    for user in await users.find({}).to_list(100):
        pprint(user)

loop = asyncio.get_event_loop()
loop.run_until_complete(find())
