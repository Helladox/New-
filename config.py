from os import getenv


API_ID = int(getenv("API_ID", "24692763"))
API_HASH = getenv("API_HASH", "8e3840420e9d0895db3231d87c6d21a5")
BOT_TOKEN = getenv("BOT_TOKEN", "7601280525:AAGK3HTLou0IzpTG1I2GShX0baxei4NExpc")
OWNER_ID = int(getenv("OWNER_ID", "8171835867"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "8171835867").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://fiona171593:tbGMvepmKQ8YNfJy@cluster0.5ccbrkf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002444252774"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002444252774"))


