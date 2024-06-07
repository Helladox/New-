from os import getenv


API_ID = int(getenv("API_ID", "24556410"))
API_HASH = getenv("API_HASH", "0aa84892224ccf16597ca8d6a9375bdf")
BOT_TOKEN = getenv("BOT_TOKEN", "7358694327:AAFkgFORP5deJ3rU1Gu3P-XfLS6euI89fEM")
OWNER_ID = int(getenv("OWNER_ID", "6750546542"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6750546542").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://fiona171593:tbGMvepmKQ8YNfJy@cluster0.5ccbrkf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002130072841"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1001764565076"))


