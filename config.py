import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6634064190:AAFjamzAKD6pZW9piaZUgbmq7WkaKTcn0")
    API_ID = int(os.environ.get("API_ID", 285007))
    API_HASH = os.environ.get("API_HASH", "38464da10310cabc8d13952419cf3")
    AUTH_USERS = os.environ.get("AUTH_USERS", "638981")
