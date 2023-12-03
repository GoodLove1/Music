import motor.motor_asyncio
from mbot import DATABASE_NAME, DATABASE_URI


class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users
        self.grp = self.db.groups


    async def add_set(self,id):
          new = {
           "id":id,
           "url": "True",
           "quality": "flac",
           "search": "True",
           "broadcast": "True",
           "http": "True",
           "done": "True",
            }
          await self.sg.insert_one(new)
    async def get_set(self,id):
          users = await self.sg.find_one({'id': int(id)})
          return users     
    async def set_set(self,id,item_id,item_type):
          await self.sg.update_one({'id': int(id)},{'$set': {item_id: item_type}})


db = Database(DATABASE_URI, DATABASE_NAME)
