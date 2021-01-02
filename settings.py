from dotenv import load_dotenv
import os
import motor.motor_asyncio

load_dotenv()

class Connection(object):
    @staticmethod
    def get_db():
        client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("URI"))
        return client.fastApi
