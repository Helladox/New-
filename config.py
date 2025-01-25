from os import getenv


API_ID = int(getenv("API_ID", "24692763"))
API_HASH = getenv("API_HASH", "8e3840420e9d0895db3231d87c6d21a5")
BOT_TOKEN = getenv("BOT_TOKEN", "7532942574:AAGCLzPvMPNtkQn_jDJTFTUWMZEPE8JJRE0")
OWNER_ID = int(getenv("OWNER_ID", "8171835867"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8171835867").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://jihehod332:OM69Q4epgIEcN3xk@cluster0.qzw02.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002307334210"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002448350703"))


