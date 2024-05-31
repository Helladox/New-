from config import MONGO_DB
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

mongo = MongoCli(MONGO_DB)
db = mongo.thumb_data
db = db.users_thumb




async def get_data(user_id):
    x = await db.find_one({"_id": user_id})
    return x
    
async def set_thumbnail(user_id, thumb):
    data = await get_data(user_id)
    if data and data.get("_id"):
        await db.update_one({"_id": user_id}, {"$set": {"thumb": thumb}})
    else:
        await db.insert_one({"_id": user_id, "thumb": thumb})


async def remove_thumbnail(user_id):
    await db.update_one({"_id": user_id}, {"$set": {"thumb": None}})

