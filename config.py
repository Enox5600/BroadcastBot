import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5897156327:AAFuF-EBhyjvqu5YADqaYdV9u3-m1-_swxk")
API_ID = int(os.environ.get("API_ID", "9321645"))
API_HASH = os.environ.get("API_HASH", "6a1b5084e59012093525c2443880a09a")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001796764763"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5296610774").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://karthickjk:karthick@cluster0.vcjskkq.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
