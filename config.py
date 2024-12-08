from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("24779895"))
API_HASH = getenv("24ca02336ac39cb748e2946de19814e3")

BOT_TOKEN = getenv("7651069480:AAEJOhBH1RxoCUl-L4HH9NhNdl8INxuKwQY")
LOG_ID = int(getenv("-4706420307", ""))

MONGO_DB_URI = getenv("mongodb+srv://ztx1430:<db_password>@cluster0.pagia.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", None)
SUDO_USER = list(map(int, getenv("7757912959", "").split()))
