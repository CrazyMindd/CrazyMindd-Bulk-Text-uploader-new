import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7010380190:AAF6nH1Ip7Ip2ER2tSGE5msGt9ZzpZWWmLg")
    API_ID = int(os.environ.get("API_ID", 20995706))
    API_HASH = os.environ.get("API_HASH", "3240c1615daa1fbbca45c34a9bb8ecf2")
    AUTH_USERS = os.environ.get("AUTH_USERS", "7184539514")
