import os

class Config:
    BOT_TOKEN = os.environ.get("1902600829:AAEQ8Ttu4ZFAeAx_rxBhw24fyv_f2KwH-SU","")
    HEROKU_API_KEY = os.environ.get("cf70b19a-3a5b-4a21-a8a3-825c1e4a405a","")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("AUTHORIZED_USERS").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("appnamersh","")
